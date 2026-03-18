

# Class al::WipeSimple



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**WipeSimple**](classal_1_1_wipe_simple.md)





* `#include <alWipeSimple.h>`



Inherits the following classes: [al::LayoutActor](classal_1_1_layout_actor.md)


















































































































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**WipeSimple**](#function-wipesimple) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name, [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* archive, [**const**](classal_1_1_functor_v0_m.md) [**LayoutInitInfo**](classal_1_1_layout_init_info.md) & info, [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* suffix=[**nullptr**](classal_1_1_functor_v0_m.md)) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**appear**](#function-appear) () <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**exeClose**](#function-execlose) () <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**exeOpen**](#function-exeopen) () <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**exeWait**](#function-exewait) () <br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isCloseEnd**](#function-iscloseend) () const<br> |


## Public Functions inherited from al::LayoutActor

See [al::LayoutActor](classal_1_1_layout_actor.md)

| Type | Name |
| ---: | :--- |
|   | [**LayoutActor**](classal_1_1_layout_actor.md#function-layoutactor) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**appear**](classal_1_1_layout_actor.md#function-appear) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**calcAnim**](classal_1_1_layout_actor.md#function-calcanim) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**control**](classal_1_1_layout_actor.md#function-control) () <br> |
| virtual [**AudioKeeper**](classal_1_1_audio_keeper.md) \* | [**getAudioKeeper**](classal_1_1_layout_actor.md#function-getaudiokeeper) () const<br> |
| virtual [**EffectKeeper**](classal_1_1_effect_keeper.md) \* | [**getEffectKeeper**](classal_1_1_layout_actor.md#function-geteffectkeeper) () const<br> |
| virtual [**NerveKeeper**](classal_1_1_nerve_keeper.md) \* | [**getNerveKeeper**](classal_1_1_layout_actor.md#function-getnervekeeper) () const<br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initNerve**](classal_1_1_layout_actor.md#function-initnerve) ([**const**](classal_1_1_functor_v0_m.md) [**Nerve**](structal_1_1_nerve.md) \* nerve, [**int**](classal_1_1_functor_v0_m.md) maxNerveStates=0) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**kill**](classal_1_1_layout_actor.md#function-kill) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**movement**](classal_1_1_layout_actor.md#function-movement) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**unk1**](classal_1_1_layout_actor.md#function-unk1) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**unk2**](classal_1_1_layout_actor.md#function-unk2) () <br> |


## Public Functions inherited from al::IUseNerve

See [al::IUseNerve](classal_1_1_i_use_nerve.md)

| Type | Name |
| ---: | :--- |
| virtual [**NerveKeeper**](classal_1_1_nerve_keeper.md) \* | [**getNerveKeeper**](classal_1_1_i_use_nerve.md#function-getnervekeeper) () const = 0<br> |


## Public Functions inherited from al::IUseAudioKeeper

See [al::IUseAudioKeeper](classal_1_1_i_use_audio_keeper.md)

| Type | Name |
| ---: | :--- |
| virtual [**AudioKeeper**](classal_1_1_audio_keeper.md) \* | [**getAudioKeeper**](classal_1_1_i_use_audio_keeper.md#function-getaudiokeeper) () const = 0<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v1**](classal_1_1_i_use_audio_keeper.md#function-v1) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v2**](classal_1_1_i_use_audio_keeper.md#function-v2) () <br> |


## Public Functions inherited from al::IUseEffectKeeper

See [al::IUseEffectKeeper](classal_1_1_i_use_effect_keeper.md)

| Type | Name |
| ---: | :--- |
| virtual [**EffectKeeper**](classal_1_1_effect_keeper.md) \* | [**getEffectKeeper**](classal_1_1_i_use_effect_keeper.md#function-geteffectkeeper) () const = 0<br> |


































## Protected Attributes inherited from al::LayoutActor

See [al::LayoutActor](classal_1_1_layout_actor.md)

| Type | Name |
| ---: | :--- |
|  [**void**](classal_1_1_functor_v0_m.md) \* | [**\_20**](classal_1_1_layout_actor.md#variable-_20)  <br> |
|  [**void**](classal_1_1_functor_v0_m.md) \* | [**\_24**](classal_1_1_layout_actor.md#variable-_24)  <br> |
|  [**void**](classal_1_1_functor_v0_m.md) \* | [**\_28**](classal_1_1_layout_actor.md#variable-_28)  <br> |
|  [**AudioKeeper**](classal_1_1_audio_keeper.md) \* | [**mAudioKeeper**](classal_1_1_layout_actor.md#variable-maudiokeeper)  <br> |
|  [**EffectKeeper**](classal_1_1_effect_keeper.md) \* | [**mEffectKeeper**](classal_1_1_layout_actor.md#variable-meffectkeeper)  <br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**mIsAlive**](classal_1_1_layout_actor.md#variable-misalive)  <br> |
|  sead::SafeString | [**mName**](classal_1_1_layout_actor.md#variable-mname)  <br> |
|  [**NerveKeeper**](classal_1_1_nerve_keeper.md) \* | [**mNerveKeeper**](classal_1_1_layout_actor.md#variable-mnervekeeper)  <br> |


































































































## Public Functions Documentation




### function WipeSimple 

```C++
al::WipeSimple::WipeSimple (
    const  char * name,
    const  char * archive,
    const  LayoutInitInfo & info,
    const  char * suffix=nullptr
) 
```




<hr>



### function appear 

```C++
virtual void al::WipeSimple::appear () 
```



Implements [*al::LayoutActor::appear*](classal_1_1_layout_actor.md#function-appear)


<hr>



### function exeClose 

```C++
void al::WipeSimple::exeClose () 
```




<hr>



### function exeOpen 

```C++
void al::WipeSimple::exeOpen () 
```




<hr>



### function exeWait 

```C++
void al::WipeSimple::exeWait () 
```




<hr>



### function isCloseEnd 

```C++
bool al::WipeSimple::isCloseEnd () const
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/include/Layout/alWipeSimple.h`

