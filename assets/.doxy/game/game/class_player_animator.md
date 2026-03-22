

# Class PlayerAnimator



[**ClassList**](annotated.md) **>** [**PlayerAnimator**](class_player_animator.md)





* `#include <PlayerAnimator.h>`



Inherits the following classes: [IUsePlayerAnimator](class_i_use_player_animator.md)






















































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**PlayerAnimator**](#function-playeranimator) (al::LiveActor \* host, [**PlayerModelHolder**](class_player_model_holder.md) \* modelHolder) <br> |
| virtual float | [**getAnimFrame**](#function-getanimframe) () const<br> |


## Public Functions inherited from IUsePlayerAnimator

See [IUsePlayerAnimator](class_i_use_player_animator.md)

| Type | Name |
| ---: | :--- |
| virtual float | [**getAnimFrame**](class_i_use_player_animator.md#function-getanimframe) () const = 0<br> |
| virtual bool | [**isAnim**](class_i_use_player_animator.md#function-isanim) (const sead::SafeString & name) = 0<br> |
| virtual bool | [**isAnimEnd**](class_i_use_player_animator.md#function-isanimend) () const = 0<br> |
| virtual void | [**v\_0**](class_i_use_player_animator.md#function-v_0) () = 0<br> |
| virtual void | [**v\_10**](class_i_use_player_animator.md#function-v_10) () = 0<br> |
| virtual void | [**v\_20**](class_i_use_player_animator.md#function-v_20) () = 0<br> |
| virtual void | [**v\_24**](class_i_use_player_animator.md#function-v_24) () = 0<br> |
| virtual void | [**v\_28**](class_i_use_player_animator.md#function-v_28) () = 0<br> |
| virtual void | [**v\_2C**](class_i_use_player_animator.md#function-v_2c) () = 0<br> |
| virtual void | [**v\_30**](class_i_use_player_animator.md#function-v_30) () = 0<br> |
| virtual void | [**v\_34**](class_i_use_player_animator.md#function-v_34) () = 0<br> |
| virtual void | [**v\_38**](class_i_use_player_animator.md#function-v_38) () = 0<br> |
| virtual void | [**v\_3C**](class_i_use_player_animator.md#function-v_3c) () = 0<br> |
| virtual void | [**v\_4**](class_i_use_player_animator.md#function-v_4) () = 0<br> |
| virtual void | [**v\_40**](class_i_use_player_animator.md#function-v_40) () = 0<br> |
| virtual void | [**v\_44**](class_i_use_player_animator.md#function-v_44) () = 0<br> |
| virtual void | [**v\_48**](class_i_use_player_animator.md#function-v_48) () = 0<br> |
| virtual void | [**v\_4C**](class_i_use_player_animator.md#function-v_4c) () = 0<br> |
| virtual void | [**v\_8**](class_i_use_player_animator.md#function-v_8) () = 0<br> |
| virtual void | [**v\_C**](class_i_use_player_animator.md#function-v_c) () = 0<br> |






















































## Public Functions Documentation




### function PlayerAnimator 

```C++
PlayerAnimator::PlayerAnimator (
    al::LiveActor * host,
    PlayerModelHolder * modelHolder
) 
```




<hr>



### function getAnimFrame 

```C++
virtual float PlayerAnimator::getAnimFrame () const
```



Implements [*IUsePlayerAnimator::getAnimFrame*](class_i_use_player_animator.md#function-getanimframe)


<hr>

------------------------------
The documentation for this class was generated from the following file `Game/backup/include/Player/PlayerAnimator.h`

