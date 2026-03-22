

# Class al::Scene



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**Scene**](classal_1_1_scene.md)





* `#include <alScene.h>`



Inherits the following classes: [al::NerveExecutor](classal_1_1_nerve_executor.md),  [al::IUseAudioKeeper](classal_1_1_i_use_audio_keeper.md)






























































































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**Scene**](#function-scene) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**appear**](#function-appear) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**control**](#function-control) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**draw3D**](#function-draw3d) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**drawEffect**](#function-draweffect) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**drawMainBottom**](#function-drawmainbottom) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**drawMainTop**](#function-drawmaintop) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**drawSubButtom**](#function-drawsubbuttom) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**drawSubTop**](#function-drawsubtop) () <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**endInit**](#function-endinit) ([**const**](classal_1_1_functor_v0_m.md) [**ActorInitInfo**](classal_1_1_actor_init_info.md) & info) <br> |
|  [**ActorFactory**](classal_1_1_actor_factory.md) \* | [**getActorFactory**](#function-getactorfactory) () const<br> |
| virtual [**AudioKeeper**](classal_1_1_audio_keeper.md) \* | [**getAudioKeeper**](#function-getaudiokeeper) () const<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**init**](#function-init) () = 0<br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initActorFactory**](#function-initactorfactory) () <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initAndLoadStageResource**](#function-initandloadstageresource) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* stageName, [**int**](classal_1_1_functor_v0_m.md) scenario, sead::Heap \* heap) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initCameraDirector**](#function-initcameradirector) () <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initLayoutKit**](#function-initlayoutkit) () <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initLiveActorKit**](#function-initliveactorkit) () <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initSceneAudio**](#function-initsceneaudio) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* stageName, [**int**](classal_1_1_functor_v0_m.md) scenario, [**int**](classal_1_1_functor_v0_m.md), [**const**](classal_1_1_functor_v0_m.md) sead::SafeString &, [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* userName) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initSceneObjHolder**](#function-initsceneobjholder) () <br> |
|  [**bool**](classal_1_1_functor_v0_m.md) | [**isAlive**](#function-isalive) () const<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**kill**](#function-kill) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**movement**](#function-movement) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**unk5**](#function-unk5) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**unk6**](#function-unk6) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**unk7**](#function-unk7) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**unk8**](#function-unk8) () <br> |


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


## Public Functions inherited from al::IUseAudioKeeper

See [al::IUseAudioKeeper](classal_1_1_i_use_audio_keeper.md)

| Type | Name |
| ---: | :--- |
| virtual [**AudioKeeper**](classal_1_1_audio_keeper.md) \* | [**getAudioKeeper**](classal_1_1_i_use_audio_keeper.md#function-getaudiokeeper) () const = 0<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v1**](classal_1_1_i_use_audio_keeper.md#function-v1) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v2**](classal_1_1_i_use_audio_keeper.md#function-v2) () <br> |










































































































## Public Functions Documentation




### function Scene 

```C++
al::Scene::Scene (
    const  char * name
) 
```




<hr>



### function appear 

```C++
virtual void al::Scene::appear () 
```




<hr>



### function control 

```C++
virtual void al::Scene::control () 
```




<hr>



### function draw3D 

```C++
inline virtual void al::Scene::draw3D () 
```




<hr>



### function drawEffect 

```C++
inline virtual void al::Scene::drawEffect () 
```




<hr>



### function drawMainBottom 

```C++
inline virtual void al::Scene::drawMainBottom () 
```




<hr>



### function drawMainTop 

```C++
inline virtual void al::Scene::drawMainTop () 
```




<hr>



### function drawSubButtom 

```C++
inline virtual void al::Scene::drawSubButtom () 
```




<hr>



### function drawSubTop 

```C++
inline virtual void al::Scene::drawSubTop () 
```




<hr>



### function endInit 

```C++
void al::Scene::endInit (
    const  ActorInitInfo & info
) 
```




<hr>



### function getActorFactory 

```C++
inline ActorFactory * al::Scene::getActorFactory () const
```




<hr>



### function getAudioKeeper 

```C++
virtual AudioKeeper * al::Scene::getAudioKeeper () const
```



Implements [*al::IUseAudioKeeper::getAudioKeeper*](classal_1_1_i_use_audio_keeper.md#function-getaudiokeeper)


<hr>



### function init 

```C++
virtual void al::Scene::init () = 0
```




<hr>



### function initActorFactory 

```C++
void al::Scene::initActorFactory () 
```




<hr>



### function initAndLoadStageResource 

```C++
void al::Scene::initAndLoadStageResource (
    const  char * stageName,
    int scenario,
    sead::Heap * heap
) 
```




<hr>



### function initCameraDirector 

```C++
void al::Scene::initCameraDirector () 
```




<hr>



### function initLayoutKit 

```C++
void al::Scene::initLayoutKit () 
```




<hr>



### function initLiveActorKit 

```C++
void al::Scene::initLiveActorKit () 
```




<hr>



### function initSceneAudio 

```C++
void al::Scene::initSceneAudio (
    const  char * stageName,
    int scenario,
    int,
    const sead::SafeString &,
    const  char * userName
) 
```




<hr>



### function initSceneObjHolder 

```C++
void al::Scene::initSceneObjHolder () 
```




<hr>



### function isAlive 

```C++
inline bool al::Scene::isAlive () const
```




<hr>



### function kill 

```C++
virtual void al::Scene::kill () 
```




<hr>



### function movement 

```C++
virtual void al::Scene::movement () 
```




<hr>



### function unk5 

```C++
inline virtual void al::Scene::unk5 () 
```




<hr>



### function unk6 

```C++
inline virtual void al::Scene::unk6 () 
```




<hr>



### function unk7 

```C++
inline virtual void al::Scene::unk7 () 
```




<hr>



### function unk8 

```C++
inline virtual void al::Scene::unk8 () 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/backup/include/Scene/alScene.h`

