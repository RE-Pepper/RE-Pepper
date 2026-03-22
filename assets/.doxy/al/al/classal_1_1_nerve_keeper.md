

# Class al::NerveKeeper



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**NerveKeeper**](classal_1_1_nerve_keeper.md)





* `#include <alNerveKeeper.h>`





































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**NerveKeeper**](#function-nervekeeper) ([**IUseNerve**](classal_1_1_i_use_nerve.md) \* host, [**const**](classal_1_1_functor_v0_m.md) [**Nerve**](structal_1_1_nerve.md) \* nrv, [**int**](classal_1_1_functor_v0_m.md) maxNerveStates=0) <br> |
|  [**NerveActionCtrl**](classal_1_1_nerve_action_ctrl.md) \* | [**getActionCtrl**](#function-getactionctrl) () <br> |
|  [**const**](classal_1_1_functor_v0_m.md) [**Nerve**](structal_1_1_nerve.md) \* | [**getCurrentNerve**](#function-getcurrentnerve) () const<br> |
|  [**IUseNerve**](classal_1_1_i_use_nerve.md) \* | [**getHost**](#function-gethost) () <br> |
|  [**NerveStateCtrl**](classal_1_1_nerve_state_ctrl.md) \* | [**getStateCtrl**](#function-getstatectrl) () <br> |
|  [**int**](classal_1_1_functor_v0_m.md) | [**getStep**](#function-getstep) () <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initNerveAction**](#function-initnerveaction) ([**NerveActionCtrl**](classal_1_1_nerve_action_ctrl.md) \* p) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**setNerve**](#function-setnerve) ([**const**](classal_1_1_functor_v0_m.md) [**Nerve**](structal_1_1_nerve.md) \* nerve) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**tryChangeNerve**](#function-trychangenerve) () <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**update**](#function-update) () <br> |




























## Public Functions Documentation




### function NerveKeeper 

```C++
al::NerveKeeper::NerveKeeper (
    IUseNerve * host,
    const  Nerve * nrv,
    int maxNerveStates=0
) 
```




<hr>



### function getActionCtrl 

```C++
inline NerveActionCtrl * al::NerveKeeper::getActionCtrl () 
```




<hr>



### function getCurrentNerve 

```C++
const  Nerve * al::NerveKeeper::getCurrentNerve () const
```




<hr>



### function getHost 

```C++
inline IUseNerve * al::NerveKeeper::getHost () 
```




<hr>



### function getStateCtrl 

```C++
inline NerveStateCtrl * al::NerveKeeper::getStateCtrl () 
```




<hr>



### function getStep 

```C++
inline int al::NerveKeeper::getStep () 
```




<hr>



### function initNerveAction 

```C++
inline void al::NerveKeeper::initNerveAction (
    NerveActionCtrl * p
) 
```




<hr>



### function setNerve 

```C++
void al::NerveKeeper::setNerve (
    const  Nerve * nerve
) 
```




<hr>



### function tryChangeNerve 

```C++
void al::NerveKeeper::tryChangeNerve () 
```




<hr>



### function update 

```C++
void al::NerveKeeper::update () 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/backup/include/Nerve/alNerveKeeper.h`

