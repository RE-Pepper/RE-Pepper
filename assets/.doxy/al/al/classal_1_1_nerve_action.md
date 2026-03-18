

# Class al::NerveAction



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**NerveAction**](classal_1_1_nerve_action.md)





* `#include <alNerveActionCtrl.h>`



Inherits the following classes: [al::Nerve](structal_1_1_nerve.md)






















































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**NerveAction**](#function-nerveaction) () <br> |
| virtual [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* | [**getName**](#function-getname) () const = 0<br> |


## Public Functions inherited from al::Nerve

See [al::Nerve](structal_1_1_nerve.md)

| Type | Name |
| ---: | :--- |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**execute**](structal_1_1_nerve.md#function-execute) ([**NerveKeeper**](classal_1_1_nerve_keeper.md) \* nerveKeeper) const = 0<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**executeOnEnd**](structal_1_1_nerve.md#function-executeonend) ([**NerveKeeper**](classal_1_1_nerve_keeper.md) \* nerveKeeper) const<br> |






















































## Public Functions Documentation




### function NerveAction 

```C++
al::NerveAction::NerveAction () 
```




<hr>



### function getName 

```C++
virtual const  char * al::NerveAction::getName () const = 0
```




<hr>## Friends Documentation





### friend NerveActionCollector 

```C++
class al::NerveAction::NerveActionCollector (
    alNerveFunction::NerveActionCollector
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/include/Nerve/alNerveActionCtrl.h`

