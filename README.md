# Overview #

## REST/JSON Protocol Variant of OPAQUE ##

Adopted from
https://docs.moodle.org/dev/Open_protocol_for_accessing_question_engines

By Andy Sayler

**Version:** 0.1.0

## Endpoints ##

| Endpoint                                    | Method | Function                                        |
| ------------------------------------------- |:------:| ----------------------------------------------- |
| `/info/`                                    | GET    | getEngineInfo()                                 |
| `/question/<base>/<qid>/<version>/`         | GET    | getQuestionMetadata(`<base>, <qid>, <version>`) |
| `/question/<base>/<qid>/<version>/session/` | POST   | start(`<base>, <qid>, <version>`)               |
| `/session/<sid>/response/`                  | PUT    | process(`<sid>`)                                |
| `/session/<sid>/`                           | DELETE | stop(`<sid>`)                                   |

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

### getQuestionMetadata(`<base>, <qid>, <version>`) ###
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

### start(`<base>, <qid>, <versions>`) ###
#### Request ####
```
    {
      'randomseed': <int>,
      'userid': '<uid>',
      'language': '<string>',
      'passKey': '<string>',
      'preferredbehavior': '<string>'
    }
```
### Response ###
```
    {
      'questionSession': '<sid>',
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

### process(`<sid>`) ###
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

### stop(`<sid>`) ###
#### Request ####
```
    <None>
```
#### Response ####
```
    <None>
```
