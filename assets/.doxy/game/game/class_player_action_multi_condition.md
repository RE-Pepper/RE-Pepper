

# Class PlayerActionMultiCondition



[**ClassList**](annotated.md) **>** [**PlayerActionMultiCondition**](class_player_action_multi_condition.md)





* `#include <PlayerActionMultiCondition.h>`



Inherits the following classes: [PlayerActionCondition](class_player_action_condition.md)






















































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**PlayerActionMultiCondition**](#function-playeractionmulticondition) () <br> |
|  void | [**append**](#function-append) ([**PlayerActionCondition**](class_player_action_condition.md) \* condition) <br> |
| virtual bool | [**check**](#function-check) () <br> |
| virtual void | [**setup**](#function-setup) () <br> |


## Public Functions inherited from PlayerActionCondition

See [PlayerActionCondition](class_player_action_condition.md)

| Type | Name |
| ---: | :--- |
| virtual bool | [**check**](class_player_action_condition.md#function-check) () = 0<br> |
| virtual void | [**setup**](class_player_action_condition.md#function-setup) () <br> |
| virtual  | [**~PlayerActionCondition**](class_player_action_condition.md#function-playeractioncondition) () <br> |






















































## Public Functions Documentation




### function PlayerActionMultiCondition 

```C++
PlayerActionMultiCondition::PlayerActionMultiCondition () 
```




<hr>



### function append 

```C++
void PlayerActionMultiCondition::append (
    PlayerActionCondition * condition
) 
```




<hr>



### function check 

```C++
virtual bool PlayerActionMultiCondition::check () 
```



Implements [*PlayerActionCondition::check*](class_player_action_condition.md#function-check)


<hr>



### function setup 

```C++
virtual void PlayerActionMultiCondition::setup () 
```



Implements [*PlayerActionCondition::setup*](class_player_action_condition.md#function-setup)


<hr>

------------------------------
The documentation for this class was generated from the following file `Game/backup/include/Player/PlayerActionMultiCondition.h`

