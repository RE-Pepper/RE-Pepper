

# Class al::NerveStateCtrl



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**NerveStateCtrl**](classal_1_1_nerve_state_ctrl.md)





* `#include <alNerveStateCtrl.h>`





































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**NerveStateCtrl**](#function-nervestatectrl) ([**int**](classal_1_1_functor_v0_m.md) capacity) <br> |
|  [**const**](classal_1_1_functor_v0_m.md) [**State**](structal_1_1_nerve_state_ctrl_1_1_state.md) \* | [**getCurrentState**](#function-getcurrentstate) () const<br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isCurrentStateEnd**](#function-iscurrentstateend) () const<br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**startState**](#function-startstate) ([**const**](classal_1_1_functor_v0_m.md) [**Nerve**](structal_1_1_nerve.md) \* nerve) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**tryEndCurrentState**](#function-tryendcurrentstate) () <br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**updateCurrentState**](#function-updatecurrentstate) () <br> |




























## Public Functions Documentation




### function NerveStateCtrl 

```C++
al::NerveStateCtrl::NerveStateCtrl (
    int capacity
) 
```




<hr>



### function getCurrentState 

```C++
inline const  State * al::NerveStateCtrl::getCurrentState () const
```




<hr>



### function isCurrentStateEnd 

```C++
bool al::NerveStateCtrl::isCurrentStateEnd () const
```




<hr>



### function startState 

```C++
void al::NerveStateCtrl::startState (
    const  Nerve * nerve
) 
```




<hr>



### function tryEndCurrentState 

```C++
void al::NerveStateCtrl::tryEndCurrentState () 
```




<hr>



### function updateCurrentState 

```C++
bool al::NerveStateCtrl::updateCurrentState () 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/backup/include/Nerve/alNerveStateCtrl.h`

