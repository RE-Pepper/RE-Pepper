

# Class PlayerTrigger



[**ClassList**](annotated.md) **>** [**PlayerTrigger**](class_player_trigger.md)





* `#include <PlayerTrigger.h>`

















## Public Types

| Type | Name |
| ---: | :--- |
| enum  | [**ECollisionTrigger**](#enum-ecollisiontrigger)  <br> |
| enum  | [**ESensorTrigger**](#enum-esensortrigger)  <br> |




















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**PlayerTrigger**](#function-playertrigger) () <br> |
|  void | [**clearCollisionTrigger**](#function-clearcollisiontrigger) () <br> |
|  void | [**clearSensorTrigger**](#function-clearsensortrigger) () <br> |
|  bool | [**isOn**](#function-ison-12) ([**PlayerTrigger::ESensorTrigger**](class_player_trigger.md#enum-esensortrigger) trigger) const<br> |
|  bool | [**isOn**](#function-ison-22) ([**PlayerTrigger::ECollisionTrigger**](class_player_trigger.md#enum-ecollisiontrigger) trigger) const<br> |
|  void | [**set**](#function-set-12) ([**PlayerTrigger::ESensorTrigger**](class_player_trigger.md#enum-esensortrigger) trigger) <br> |
|  void | [**set**](#function-set-22) ([**PlayerTrigger::ECollisionTrigger**](class_player_trigger.md#enum-ecollisiontrigger) trigger) <br> |




























## Public Types Documentation




### enum ECollisionTrigger 

```C++
enum PlayerTrigger::ECollisionTrigger;
```




<hr>



### enum ESensorTrigger 

```C++
enum PlayerTrigger::ESensorTrigger;
```




<hr>
## Public Functions Documentation




### function PlayerTrigger 

```C++
PlayerTrigger::PlayerTrigger () 
```




<hr>



### function clearCollisionTrigger 

```C++
void PlayerTrigger::clearCollisionTrigger () 
```




<hr>



### function clearSensorTrigger 

```C++
void PlayerTrigger::clearSensorTrigger () 
```




<hr>



### function isOn [1/2]

```C++
bool PlayerTrigger::isOn (
    PlayerTrigger::ESensorTrigger trigger
) const
```




<hr>



### function isOn [2/2]

```C++
bool PlayerTrigger::isOn (
    PlayerTrigger::ECollisionTrigger trigger
) const
```




<hr>



### function set [1/2]

```C++
void PlayerTrigger::set (
    PlayerTrigger::ESensorTrigger trigger
) 
```




<hr>



### function set [2/2]

```C++
void PlayerTrigger::set (
    PlayerTrigger::ECollisionTrigger trigger
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `Game/backup/include/Player/PlayerTrigger.h`

