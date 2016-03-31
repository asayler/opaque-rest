# Overview #

## REST/JSON Protocol Variant of OPAQUE ##

Adopted from
https://docs.moodle.org/dev/Open_protocol_for_accessing_question_engines

By Andy Sayler

**Version:** 0.1.0

## Endpoints ##

| Endpoint                                   | Method | Function              |
| ------------------------------------------ |:------:| --------------------- |
| `/info/`                                   | GET    | getEngineInfo()       |
| `/question/<base>/<id>/<version>/`         | GET    | getQuestionMetadata() |
| `/question/<base>/<id>/<version>/session/` | POST   | start()               |
| `/session/<id>/response/`                  | PUT    | process()             |
| `/session/<id>/`                           | DELETE | stop()                |

## Functions ##

### getEngineInfo() ###
#### Request ####
```
    <None>
```
#### Response ####
```
    { 
      'name': '<string>',
      'usedmemory': '<string>', (optional)
      'activesessions': <int> (optional)
    }
```

### getQuestionMetadata(<base>, <id>, <version>) ###
#### Request ####
```
    <None>
```
#### Response ####
```
    { 
      'scoring': {
                   'marks': <int>
                 },
      'plainmode': <true|false>
    }
```

### start(<base>, <id>, <versions>) ###
#### Request ####
```
    {
      'randomseed': <int>,
      'userid': '<string>',
      'language': '<string>',
      'passKey': '<string>',
      'preferredbehavior': '<string>'
    }
```
### Response ###
```
    {
      'questionSession': '<string>',
      'XHTML': '<string>',
      'CSS': '<string>',
      'progressInfo': '<string>',
      'resources': [
                     {
                       'content': '<base64>',
                       'encoding': '<string>',
                       'filename': '<string>'
                       'mimetype': '<string>'
                     },
                     ...
                   ]
    }
```

### process(<id>) ###
#### Request ####
```
    {
      'key1': 'val1',
      'key2': 'val2',
      ...
    }
```
#### Response ####
```
    {
      'XHTML': '<string>',
      'CSS': '<string>',
      'progressInfo': '<string>',
      'questionEnd': <true|false>
      'resources': [
                     {
                       'content': '<base64>',
                       'encoding': '<string>',
                       'filename': '<string>'
                       'mimetype': '<string>'
                     },
                     ...
                   ]
      'results': [
                   {
                     'questionLine': '<string>',
                     'answerLine': '<string>',
                     'actionSummary': '<string>',
                     'attempts': <int>,
                     'scores': {
                                 '<string>': <float>,
                                 ...
                               }
                     'customResults': {
                                        '<string>': <string>,
                                         ...
                                       }
                   }
                 ]
    }
```

### stop(<id>) ###
#### Request ####
```
    <None>
```
#### Response ####
```
    <None>
```
