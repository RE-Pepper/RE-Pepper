

# Class PlayerActionConditionAnimEnd



[**ClassList**](annotated.md) **>** [**PlayerActionConditionAnimEnd**](class_player_action_condition_anim_end.md)





* `#include <PlayerActionConditionAnimEnd.h>`



Inherits the following classes: [PlayerActionCondition](class_player_action_condition.md)






















































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**PlayerActionConditionAnimEnd**](#function-playeractionconditionanimend) ([**IUsePlayerAnimator**](class_i_use_player_animator.md) \* animator, [**const**](class_player_action_condition_anim_end.md#variable-manimendframe) [**char**](class_player_action_condition_anim_end.md#variable-manimendframe) \* animName, [**int**](class_player_action_condition_anim_end.md#variable-manimendframe) animEndFrame) <br> |
| virtual [**bool**](class_player_action_condition_anim_end.md#variable-manimendframe) | [**check**](#function-check) () <br> |


## Public Functions inherited from PlayerActionCondition

See [PlayerActionCondition](class_player_action_condition.md)

| Type | Name |
| ---: | :--- |
| virtual bool | [**check**](class_player_action_condition.md#function-check) () = 0<br> |
| virtual void | [**setup**](class_player_action_condition.md#function-setup) () <br> |
| virtual  | [**~PlayerActionCondition**](class_player_action_condition.md#function-playeractioncondition) () <br> |






















































## Public Functions Documentation




### function PlayerActionConditionAnimEnd 

```C++
PlayerActionConditionAnimEnd::PlayerActionConditionAnimEnd (
    IUsePlayerAnimator * animator,
    const  char * animName,
    int animEndFrame
) 
```




<hr>



### function check 

```C++
virtual bool PlayerActionConditionAnimEnd::check () 
```



Implements [*PlayerActionCondition::check*](class_player_action_condition.md#function-check)


<hr>

------------------------------
The documentation for this class was generated from the following file `Game/backup/include/Player/PlayerActionConditionAnimEnd.h`

