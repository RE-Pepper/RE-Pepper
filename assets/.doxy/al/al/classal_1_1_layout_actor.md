

# Class al::LayoutActor



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**LayoutActor**](classal_1_1_layout_actor.md)





* `#include <alLayoutActor.h>`



Inherits the following classes: [al::IUseNerve](classal_1_1_i_use_nerve.md),  [al::IUseAudioKeeper](classal_1_1_i_use_audio_keeper.md),  [al::IUseEffectKeeper](classal_1_1_i_use_effect_keeper.md)


Inherited by the following classes: [al::WipeSimple](classal_1_1_wipe_simple.md)




























































































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**LayoutActor**](#function-layoutactor) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**appear**](#function-appear) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**calcAnim**](#function-calcanim) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**control**](#function-control) () <br> |
| virtual [**AudioKeeper**](classal_1_1_audio_keeper.md) \* | [**getAudioKeeper**](#function-getaudiokeeper) () const<br> |
| virtual [**EffectKeeper**](classal_1_1_effect_keeper.md) \* | [**getEffectKeeper**](#function-geteffectkeeper) () const<br> |
| virtual [**NerveKeeper**](classal_1_1_nerve_keeper.md) \* | [**getNerveKeeper**](#function-getnervekeeper) () const<br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initNerve**](#function-initnerve) ([**const**](classal_1_1_functor_v0_m.md) [**Nerve**](structal_1_1_nerve.md) \* nerve, [**int**](classal_1_1_functor_v0_m.md) maxNerveStates=0) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**kill**](#function-kill) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**movement**](#function-movement) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**unk1**](#function-unk1) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**unk2**](#function-unk2) () <br> |


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


























## Protected Attributes

| Type | Name |
| ---: | :--- |
|  [**void**](classal_1_1_functor_v0_m.md) \* | [**\_20**](#variable-_20)  <br> |
|  [**void**](classal_1_1_functor_v0_m.md) \* | [**\_24**](#variable-_24)  <br> |
|  [**void**](classal_1_1_functor_v0_m.md) \* | [**\_28**](#variable-_28)  <br> |
|  [**AudioKeeper**](classal_1_1_audio_keeper.md) \* | [**mAudioKeeper**](#variable-maudiokeeper)  <br> |
|  [**EffectKeeper**](classal_1_1_effect_keeper.md) \* | [**mEffectKeeper**](#variable-meffectkeeper)  <br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**mIsAlive**](#variable-misalive)  <br> |
|  sead::SafeString | [**mName**](#variable-mname)  <br> |
|  [**NerveKeeper**](classal_1_1_nerve_keeper.md) \* | [**mNerveKeeper**](#variable-mnervekeeper)  <br> |
















































































## Public Functions Documentation




### function LayoutActor 

```C++
al::LayoutActor::LayoutActor (
    const  char * name
) 
```




<hr>



### function appear 

```C++
virtual void al::LayoutActor::appear () 
```




<hr>



### function calcAnim 

```C++
virtual void al::LayoutActor::calcAnim () 
```




<hr>



### function control 

```C++
virtual void al::LayoutActor::control () 
```




<hr>



### function getAudioKeeper 

```C++
virtual AudioKeeper * al::LayoutActor::getAudioKeeper () const
```



Implements [*al::IUseAudioKeeper::getAudioKeeper*](classal_1_1_i_use_audio_keeper.md#function-getaudiokeeper)


<hr>



### function getEffectKeeper 

```C++
virtual EffectKeeper * al::LayoutActor::getEffectKeeper () const
```



Implements [*al::IUseEffectKeeper::getEffectKeeper*](classal_1_1_i_use_effect_keeper.md#function-geteffectkeeper)


<hr>



### function getNerveKeeper 

```C++
virtual NerveKeeper * al::LayoutActor::getNerveKeeper () const
```



Implements [*al::IUseNerve::getNerveKeeper*](classal_1_1_i_use_nerve.md#function-getnervekeeper)


<hr>



### function initNerve 

```C++
void al::LayoutActor::initNerve (
    const  Nerve * nerve,
    int maxNerveStates=0
) 
```




<hr>



### function kill 

```C++
virtual void al::LayoutActor::kill () 
```




<hr>



### function movement 

```C++
virtual void al::LayoutActor::movement () 
```




<hr>



### function unk1 

```C++
virtual void al::LayoutActor::unk1 () 
```




<hr>



### function unk2 

```C++
virtual void al::LayoutActor::unk2 () 
```




<hr>
## Protected Attributes Documentation




### variable \_20 

```C++
void* al::LayoutActor::_20;
```




<hr>



### variable \_24 

```C++
void* al::LayoutActor::_24;
```




<hr>



### variable \_28 

```C++
void* al::LayoutActor::_28;
```




<hr>



### variable mAudioKeeper 

```C++
AudioKeeper* al::LayoutActor::mAudioKeeper;
```




<hr>



### variable mEffectKeeper 

```C++
EffectKeeper* al::LayoutActor::mEffectKeeper;
```




<hr>



### variable mIsAlive 

```C++
bool al::LayoutActor::mIsAlive;
```




<hr>



### variable mName 

```C++
sead::SafeString al::LayoutActor::mName;
```




<hr>



### variable mNerveKeeper 

```C++
NerveKeeper* al::LayoutActor::mNerveKeeper;
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/backup/include/Layout/alLayoutActor.h`

