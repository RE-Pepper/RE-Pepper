

# Class al::RailMoveMovement



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**RailMoveMovement**](classal_1_1_rail_move_movement.md)





* `#include <alRailMoveMovement.h>`



Inherits the following classes: [al::HostStateBase](classal_1_1_host_state_base.md)


















































































































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**RailMoveMovement**](#function-railmovemovement) ([**LiveActor**](classal_1_1_live_actor.md) \* host, [**const**](classal_1_1_functor_v0_m.md) [**ActorInitInfo**](classal_1_1_actor_init_info.md) & info, [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* speedParamName="Arg0", [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* moveTypeParamName="Arg1") <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**exeMove**](#function-exemove) () <br> |


## Public Functions inherited from al::HostStateBase

See [al::HostStateBase](classal_1_1_host_state_base.md)

| Type | Name |
| ---: | :--- |
|   | [**HostStateBase**](classal_1_1_host_state_base.md#function-hoststatebase) ([**T**](classal_1_1_functor_v0_m.md) \* host, [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name) <br> |


## Public Functions inherited from al::NerveStateBase

See [al::NerveStateBase](classal_1_1_nerve_state_base.md)

| Type | Name |
| ---: | :--- |
|   | [**NerveStateBase**](classal_1_1_nerve_state_base.md#function-nervestatebase) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**appear**](classal_1_1_nerve_state_base.md#function-appear) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**control**](classal_1_1_nerve_state_base.md#function-control) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**init**](classal_1_1_nerve_state_base.md#function-init) () <br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isDead**](classal_1_1_nerve_state_base.md#function-isdead) () const<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**kill**](classal_1_1_nerve_state_base.md#function-kill) () <br> |
| virtual [**bool**](classal_1_1_functor_v0_m.md) | [**update**](classal_1_1_nerve_state_base.md#function-update) () <br> |


## Public Functions inherited from al::NerveExecutor

See [al::NerveExecutor](classal_1_1_nerve_executor.md)

| Type | Name |
| ---: | :--- |
|   | [**NerveExecutor**](classal_1_1_nerve_executor.md#function-nerveexecutor) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name) <br> |
| virtual [**NerveKeeper**](classal_1_1_nerve_keeper.md) \* | [**getNerveKeeper**](classal_1_1_nerve_executor.md#function-getnervekeeper) () const<br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initNerve**](classal_1_1_nerve_executor.md#function-initnerve) ([**const**](classal_1_1_functor_v0_m.md) [**Nerve**](structal_1_1_nerve.md) \* nrv, [**int**](classal_1_1_functor_v0_m.md) step=0) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**updateNerve**](classal_1_1_nerve_executor.md#function-updatenerve) () <br> |
| virtual  | [**~NerveExecutor**](classal_1_1_nerve_executor.md#function-nerveexecutor) () <br> |


## Public Functions inherited from al::IUseNerve

See [al::IUseNerve](classal_1_1_i_use_nerve.md)

| Type | Name |
| ---: | :--- |
| virtual [**NerveKeeper**](classal_1_1_nerve_keeper.md) \* | [**getNerveKeeper**](classal_1_1_i_use_nerve.md#function-getnervekeeper) () const = 0<br> |


































## Protected Attributes inherited from al::HostStateBase

See [al::HostStateBase](classal_1_1_host_state_base.md)

| Type | Name |
| ---: | :--- |
|  [**T**](classal_1_1_functor_v0_m.md) \*[**const**](classal_1_1_functor_v0_m.md) | [**mHost**](classal_1_1_host_state_base.md#variable-mhost)  <br> |


































































































## Public Functions Documentation




### function RailMoveMovement 

```C++
al::RailMoveMovement::RailMoveMovement (
    LiveActor * host,
    const  ActorInitInfo & info,
    const  char * speedParamName="Arg0",
    const  char * moveTypeParamName="Arg1"
) 
```




<hr>



### function exeMove 

```C++
void al::RailMoveMovement::exeMove () 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/include/Rail/alRailMoveMovement.h`

