import sublime, sublime_plugin

class FormatApexLogCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.format(edit)
        self.foldAllTags()
        self.highlightDebugs()
        
    def format(self, edit):
        # get all contents of view as a list of lines
        view = self.view
        wholeViewRegion = sublime.Region(0, view.size())
        lines = self.view.lines(wholeViewRegion)

        formattedString = ''
        for line in lines:
            # format the contents
            contents = '\n' + view.substr(line) + '\n'
            if 'USER_DEBUG' in contents or 'FATAL_ERROR' in contents:
                formattedString += self.formatLine(contents)
            elif 'SYSTEM_MODE_' not in contents:
                # don't include System mode in formatted contents
                formattedString +=  contents

        # replace contents with the formatted contents
        view.replace(edit, wholeViewRegion, '\n' + formattedString)

    def formatLine(self, contents):
        numTabs = 0
        tab = ' ' * 4
        formattedString = ''
        
        if ('|DEBUG|' in contents):
            split = '|DEBUG|'
        elif ('|INFO|' in contents):
            split = '|INFO|'
        elif ('|WARN|' in contents):
            split = '|WARN|'

        contentsSplit = contents.split(split)
        if (len(contentsSplit) != 2):
            contentsSplit = contents.split('|FATAL_ERROR|')
        if (len(contentsSplit) != 2):
            return contents
        else:
            formattedString += contentsSplit[0]
            contents = contentsSplit[1]
        skipNext = False
        for index, char in enumerate(contents):
            if skipNext:
                skipNext = False
                continue

            previousChar, nextChar = None, None
            if index > 0:
                previousChar = contents[index - 1]
            if index < (index - 1):
                nextChar = contents[index + 1]

            if char == '(' and nextChar == ')':
                 formattedString += '()'
                 skipNext = True
                 continue

            if char in ['{', '}', ']', '[', '(', ')']:
                if char in ['}', ')', ']']:
                    numTabs -= 1
                formattedString += '\n' + (tab * numTabs) + char
                if char in ['{', '(', '[']:
                    numTabs += 1
                formattedString += '\n' + (tab * numTabs)
            elif char == ',' and numTabs > 0:
                formattedString += ',\n' + (tab * numTabs)
            else:
                formattedString += char
        return formattedString

    def foldAllTags(self):
        view = self.view
        self.foldTag('CUMULATIVE_LIMIT_USAGE', 'CUMULATIVE_LIMIT_USAGE_END')
        self.foldTag('SOQL_EXECUTE_BEGIN', 'SOQL_EXECUTE_END')
        self.foldTag('\|CODE_UNIT_STARTED\|\[EXTERNAL\]\|Validation', '\|CODE_UNIT_FINISHED\|Validation')
        self.foldTag('SELECT', 'FROM')

    def foldTag(self, startTag, endTag):
        # get the all regions starting with start tag
        regions = self.view.find_all('(?s)' + startTag + '.*?' + endTag)
        # for each region, fold content between tags
        for region in regions:
            regionBetweenTags = sublime.Region(
                region.begin() + len(startTag), 
                region.end() - len(endTag))
            self.view.fold(regionBetweenTags)

    def highlightDebugs(self):
        regions = self.view.find_all('USER_DEBUG')
        self.view.add_regions("WordHighlight", regions, "comment", 'dot')
