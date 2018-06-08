Format Apex Log
=============

Sublime text plugin that formats, highlights and folds apex log files.

Apex logs are difficult to read without additional spacing, this plugin will make apex logs easier to read. The plugin:
    
* formats JSON objects in USER_DEBUG or FATAL_ERROR log lines by adding a new line and increasing indentation after '(', '{', '[', and adding a new line and decreasing indendation after ')', '}', or ']'. 
* removes lines containing ENTER_SYSTEM_MODE and EXIT_SYSTEM_MODE
* folds 
    * 'CUMULATIVE_LIMIT_USAGE' to 'CUMULATIVE_LIMIT_USAGE_END'
    * 'SOQL_EXECUTE_BEGIN' to 'SOQL_EXECUTE_END'
    * validation rule blocks in triggers 
    * 'SELECT' to 'FROM', to hide long field lists in debugged queries
* highlights USER_DEBUG statements 

Installation
============

- Clone source code to Sublime Text packages folder.

Usage
=====

Use one of the following:
- Bring up the command palette (it's `⌘ + shift + p`  in OS X and `ctrl + shift + p` in Windows or Linux) and type `format-apex-log` and select `format-apex-log: Format This Apex Log` command.
- Use `ctrl + alt + e
