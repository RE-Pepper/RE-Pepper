

# Class NoteObj



[**ClassList**](annotated.md) **>** [**NoteObj**](class_note_obj.md)





* `#include <NoteObj.h>`



Inherits the following classes: al::MapObjActor


































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**NoteObj**](#function-noteobj-12) (const char \* name) <br> |
|   | [**NoteObj**](#function-noteobj-22) ([**NoteObjGenerator**](class_note_obj_generator.md) \* generator) <br> |
| virtual void | [**control**](#function-control) () <br> |
| virtual void | [**init**](#function-init) (const al::ActorInitInfo & info) <br> |
| virtual void | [**initAfterPlacement**](#function-initafterplacement) () <br> |
| virtual bool | [**receiveMsg**](#function-receivemsg) (u32 msg, al::HitSensor \* other, al::HitSensor \* me) <br> |




























## Public Functions Documentation




### function NoteObj [1/2]

```C++
NoteObj::NoteObj (
    const char * name
) 
```




<hr>



### function NoteObj [2/2]

```C++
NoteObj::NoteObj (
    NoteObjGenerator * generator
) 
```




<hr>



### function control 

```C++
virtual void NoteObj::control () 
```




<hr>



### function init 

```C++
virtual void NoteObj::init (
    const al::ActorInitInfo & info
) 
```




<hr>



### function initAfterPlacement 

```C++
virtual void NoteObj::initAfterPlacement () 
```




<hr>



### function receiveMsg 

```C++
virtual bool NoteObj::receiveMsg (
    u32 msg,
    al::HitSensor * other,
    al::HitSensor * me
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `Game/backup/include/MapObj/NoteObj.h`

