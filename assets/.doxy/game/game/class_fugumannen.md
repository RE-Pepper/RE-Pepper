

# Class Fugumannen



[**ClassList**](annotated.md) **>** [**Fugumannen**](class_fugumannen.md)





* `#include <Fugumannen.h>`



Inherits the following classes: al::MapObjActor


































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**Fugumannen**](#function-fugumannen) (const sead::SafeString & name) <br> |
| virtual void | [**attackSensor**](#function-attacksensor) (al::HitSensor \* me, al::HitSensor \* other) <br> |
|  void | [**exeBlowDown**](#function-exeblowdown) () <br> |
|  void | [**exeMove**](#function-exemove) () <br> |
|  void | [**exeMove2**](#function-exemove2) () <br> |
| virtual void | [**init**](#function-init) (const al::ActorInitInfo & info) <br> |
| virtual bool | [**receiveMsg**](#function-receivemsg) (u32 msg, al::HitSensor \* other, al::HitSensor \* me) <br> |




























## Public Functions Documentation




### function Fugumannen 

```C++
Fugumannen::Fugumannen (
    const sead::SafeString & name
) 
```




<hr>



### function attackSensor 

```C++
virtual void Fugumannen::attackSensor (
    al::HitSensor * me,
    al::HitSensor * other
) 
```




<hr>



### function exeBlowDown 

```C++
void Fugumannen::exeBlowDown () 
```




<hr>



### function exeMove 

```C++
void Fugumannen::exeMove () 
```




<hr>



### function exeMove2 

```C++
void Fugumannen::exeMove2 () 
```




<hr>



### function init 

```C++
virtual void Fugumannen::init (
    const al::ActorInitInfo & info
) 
```




<hr>



### function receiveMsg 

```C++
virtual bool Fugumannen::receiveMsg (
    u32 msg,
    al::HitSensor * other,
    al::HitSensor * me
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `Game/backup/include/Enemy/Fugumannen.h`

