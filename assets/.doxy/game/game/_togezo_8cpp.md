

# File Togezo.cpp



[**FileList**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**Enemy**](dir_0e41e8db2a159a2532eb8129063edf58.md) **>** [**Togezo.cpp**](_togezo_8cpp.md)

[Go to the source code of this file](_togezo_8cpp_source.md)



* `#include "Enemy/Togezo.h"`
* `#include <LiveActor/alActorInitUtil.h>`
* `#include <LiveActor/alActorPoseKeeper.h>`
* `#include <LiveActor/alLiveActorFunction.h>`
* `#include <Nerve/alNerve.h>`
* `#include <Nerve/alNerveFunction.h>`
* `#include <Nerve/alNerveStateBase.h>`
* `#include <math/seadVector.h>`
* `#include "Enemy/EnemyStateBlowDown.h"`
* `#include "Enemy/WalkerStateChase.h"`
* `#include "Enemy/WalkerStateChaseParam.h"`
* `#include "Enemy/WalkerStateParam.h"`
* `#include "Enemy/WalkerStateWander.h"`
* `#include "Enemy/WalkerStateWanderParam.h"`
* `#include "Player/PlayerFunction.h"`













## Namespaces

| Type | Name |
| ---: | :--- |
| namespace | [**NrvTogezo**](namespace_nrv_togezo.md) <br> |
























## Public Functions

| Type | Name |
| ---: | :--- |
|  void | [**fn\_00258774**](#function-fn_00258774) ([**Togezo**](class_togezo.md) \*, const [**WalkerStateParam**](class_walker_state_param.md) \*) <br> |
|  bool | [**fn\_00259758**](#function-fn_00259758) (al::LiveActor \*, const sead::Vector3f &, const [**WalkerStateParam**](class_walker_state_param.md) \*) <br> |
|  bool | [**fn\_00262988**](#function-fn_00262988) (al::LiveActor \*, sead::Vector3f \* out, const sead::Vector3f &, float) <br> |
|  bool | [**fn\_0026b6cc**](#function-fn_0026b6cc) ([**WalkerStateWander**](class_walker_state_wander.md) \*, const sead::Vector3f & trans) <br> |
|  bool | [**fn\_00272a9c**](#function-fn_00272a9c) () <br> |
|  void | [**fn\_00279158**](#function-fn_00279158) ([**Togezo**](class_togezo.md) \*, const [**EnemyStateBlowDown**](class_enemy_state_blow_down.md) \*) <br> |
|  void | [**fn\_0027a1a0**](#function-fn_0027a1a0) (al::LiveActor \* actor, const char \*) <br> |
|  void | [**fn\_0027cf20**](#function-fn_0027cf20) (al::LiveActor \* actor, const al::ActorInitInfo & info, int) <br> |


## Public Static Functions

| Type | Name |
| ---: | :--- |
|  [**WalkerStateChaseParam**](class_walker_state_chase_param.md) sdata() | [**sTogezoWalkerStateChaseParam**](#function-stogezowalkerstatechaseparam) (false, true, 1. 3, 30. 0, 150. 0, 3. 0, 20. 0, "Run", "Wait") <br> |
|  [**WalkerStateParam**](class_walker_state_param.md) sdata() | [**sTogezoWalkerStateParam**](#function-stogezowalkerstateparam) (4. 0, 0. 98, 0. 85, 250. 0, 700. 0, 180. 0, 70. 0, 150. 0) <br> |
|  [**WalkerStateWanderParam**](class_walker_state_wander_param.md) sdata() | [**sTogezoWalkerStateWanderParam**](#function-stogezowalkerstatewanderparam) (30, 90, 0. 7, 4. 0, 10. 0, "Walk", "Wait") <br> |


























## Public Functions Documentation




### function fn\_00258774 

```C++
void fn_00258774 (
    Togezo *,
    const WalkerStateParam *
) 
```




<hr>



### function fn\_00259758 

```C++
bool fn_00259758 (
    al::LiveActor *,
    const sead::Vector3f &,
    const WalkerStateParam *
) 
```




<hr>



### function fn\_00262988 

```C++
bool fn_00262988 (
    al::LiveActor *,
    sead::Vector3f * out,
    const sead::Vector3f &,
    float
) 
```




<hr>



### function fn\_0026b6cc 

```C++
bool fn_0026b6cc (
    WalkerStateWander *,
    const sead::Vector3f & trans
) 
```




<hr>



### function fn\_00272a9c 

```C++
bool fn_00272a9c () 
```




<hr>



### function fn\_00279158 

```C++
void fn_00279158 (
    Togezo *,
    const EnemyStateBlowDown *
) 
```




<hr>



### function fn\_0027a1a0 

```C++
void fn_0027a1a0 (
    al::LiveActor * actor,
    const char *
) 
```




<hr>



### function fn\_0027cf20 

```C++
void fn_0027cf20 (
    al::LiveActor * actor,
    const al::ActorInitInfo & info,
    int
) 
```




<hr>
## Public Static Functions Documentation




### function sTogezoWalkerStateChaseParam 

```C++
static WalkerStateChaseParam sdata() sTogezoWalkerStateChaseParam (
    false,
    true,
    1. 3,
    30. 0,
    150. 0,
    3. 0,
    20. 0,
    "Run",
    "Wait"
) 
```




<hr>



### function sTogezoWalkerStateParam 

```C++
static WalkerStateParam sdata() sTogezoWalkerStateParam (
    4. 0,
    0. 98,
    0. 85,
    250. 0,
    700. 0,
    180. 0,
    70. 0,
    150. 0
) 
```




<hr>



### function sTogezoWalkerStateWanderParam 

```C++
static WalkerStateWanderParam sdata() sTogezoWalkerStateWanderParam (
    30,
    90,
    0. 7,
    4. 0,
    10. 0,
    "Walk",
    "Wait"
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `Game/backup/src/Enemy/Togezo.cpp`

