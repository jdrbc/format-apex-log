Format Apex Log
=============

Sublime text plugin that formats, highlights and folds [apex log files](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_debugging_debug_log.htm).

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

* Install via [sublime text package control](https://packagecontrol.io/packages/Format%20Apex%20Log) search for 'format apex log'
* To manually install clone source code to Sublime Text packages folder.

Usage
=====

Use one of the following:
* Bring up the command palette (it's `⌘ + shift + p`  in OS X and `ctrl + shift + p` in Windows or Linux) and type `format-apex-log` and select `format-apex-log: Format This Apex Log` command.
* Use `ctrl + alt + e`
