

# Class al::MapObjActor



[**ClassList**](annotated.md) **>** [**al**](namespaceal.md) **>** [**MapObjActor**](classal_1_1_map_obj_actor.md)





* `#include <alMapObjActor.h>`



Inherits the following classes: [al::LiveActor](classal_1_1_live_actor.md)


Inherited by the following classes: [al::ClockMapParts](classal_1_1_clock_map_parts.md),  [al::EffectObj](classal_1_1_effect_obj.md),  [al::FallMapParts](classal_1_1_fall_map_parts.md),  [al::FixMapParts](classal_1_1_fix_map_parts.md),  [al::Sky](classal_1_1_sky.md)




































































































































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**MapObjActor**](#function-mapobjactor) ([**const**](classal_1_1_functor_v0_m.md) sead::SafeString & name) <br> |


## Public Functions inherited from al::LiveActor

See [al::LiveActor](classal_1_1_live_actor.md)

| Type | Name |
| ---: | :--- |
|   | [**LiveActor**](classal_1_1_live_actor.md#function-liveactor) ([**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* name) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**appear**](classal_1_1_live_actor.md#function-appear) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**attackSensor**](classal_1_1_live_actor.md#function-attacksensor) ([**HitSensor**](classal_1_1_hit_sensor.md) \* me, [**HitSensor**](classal_1_1_hit_sensor.md) \* other) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**calcAndSetBaseMtx**](classal_1_1_live_actor.md#function-calcandsetbasemtx) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**calcAnim**](classal_1_1_live_actor.md#function-calcanim) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**control**](classal_1_1_live_actor.md#function-control) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**draw**](classal_1_1_live_actor.md#function-draw) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**endClipped**](classal_1_1_live_actor.md#function-endclipped) () <br> |
|  [**ActorActionKeeper**](classal_1_1_actor_action_keeper.md) \* | [**getActorActionKeeper**](classal_1_1_live_actor.md#function-getactoractionkeeper) () const<br> |
|  [**ActorExecuteInfo**](classal_1_1_actor_execute_info.md) \* | [**getActorExecuteInfo**](classal_1_1_live_actor.md#function-getactorexecuteinfo) () const<br> |
|  [**ActorPoseKeeperBase**](classal_1_1_actor_pose_keeper_base.md) \* | [**getActorPoseKeeper**](classal_1_1_live_actor.md#function-getactorposekeeper) () const<br> |
| virtual [**AudioKeeper**](classal_1_1_audio_keeper.md) \* | [**getAudioKeeper**](classal_1_1_live_actor.md#function-getaudiokeeper) () const<br> |
| virtual [**const**](classal_1_1_functor_v0_m.md) sead::Matrix34f \* | [**getBaseMtx**](classal_1_1_live_actor.md#function-getbasemtx) () const<br> |
|  [**Collider**](classal_1_1_collider.md) \* | [**getCollider**](classal_1_1_live_actor.md#function-getcollider) () const<br> |
| virtual [**EffectKeeper**](classal_1_1_effect_keeper.md) \* | [**getEffectKeeper**](classal_1_1_live_actor.md#function-geteffectkeeper) () const<br> |
|  [**HitSensorKeeper**](classal_1_1_hit_sensor_keeper.md) \* | [**getHitSensorKeeper**](classal_1_1_live_actor.md#function-gethitsensorkeeper) () const<br> |
|  [**LiveActorFlag**](structal_1_1_live_actor_flag.md) & | [**getLiveActorFlag**](classal_1_1_live_actor.md#function-getliveactorflag-12) () <br> |
|  [**const**](classal_1_1_functor_v0_m.md) [**LiveActorFlag**](structal_1_1_live_actor_flag.md) & | [**getLiveActorFlag**](classal_1_1_live_actor.md#function-getliveactorflag-22) () const<br> |
|  [**ModelKeeper**](classal_1_1_model_keeper.md) \* | [**getModelKeeper**](classal_1_1_live_actor.md#function-getmodelkeeper) () const<br> |
|  [**const**](classal_1_1_functor_v0_m.md) [**char**](classal_1_1_functor_v0_m.md) \* | [**getName**](classal_1_1_live_actor.md#function-getname) () const<br> |
| virtual [**NerveKeeper**](classal_1_1_nerve_keeper.md) \* | [**getNerveKeeper**](classal_1_1_live_actor.md#function-getnervekeeper) () const<br> |
|  [**RailKeeper**](classal_1_1_rail_keeper.md) \* | [**getRailKeeper**](classal_1_1_live_actor.md#function-getrailkeeper) () const<br> |
|  [**ShadowKeeper**](classal_1_1_shadow_keeper.md) \* | [**getShadowKeeper**](classal_1_1_live_actor.md#function-getshadowkeeper) () const<br> |
| virtual [**StageSwitchKeeper**](classal_1_1_stage_switch_keeper.md) \* | [**getStageSwitchKeeper**](classal_1_1_live_actor.md#function-getstageswitchkeeper) () const<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**init**](classal_1_1_live_actor.md#function-init) ([**const**](classal_1_1_functor_v0_m.md) [**ActorInitInfo**](classal_1_1_actor_init_info.md) & info) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**initAfterPlacement**](classal_1_1_live_actor.md#function-initafterplacement) () <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initCollider**](classal_1_1_live_actor.md#function-initcollider) ([**float**](classal_1_1_functor_v0_m.md) radius, [**float**](classal_1_1_functor_v0_m.md) yOffset, [**u32**](classal_1_1_functor_v0_m.md)) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initNerveKeeper**](classal_1_1_live_actor.md#function-initnervekeeper) ([**NerveKeeper**](classal_1_1_nerve_keeper.md) \* nk) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initPoseKeeper**](classal_1_1_live_actor.md#function-initposekeeper) ([**ActorPoseKeeperBase**](classal_1_1_actor_pose_keeper_base.md) \* pPoseKeeper) <br> |
|  [**void**](classal_1_1_functor_v0_m.md) | [**initRailKeeper**](classal_1_1_live_actor.md#function-initrailkeeper) ([**const**](classal_1_1_functor_v0_m.md) [**ActorInitInfo**](classal_1_1_actor_init_info.md) & info) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**initStageSwitchKeeper**](classal_1_1_live_actor.md#function-initstageswitchkeeper) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**kill**](classal_1_1_live_actor.md#function-kill) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**makeActorAppeared**](classal_1_1_live_actor.md#function-makeactorappeared) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**makeActorDead**](classal_1_1_live_actor.md#function-makeactordead) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**movement**](classal_1_1_live_actor.md#function-movement) () <br> |
| virtual [**bool**](classal_1_1_functor_v0_m.md) | [**receiveMsg**](classal_1_1_live_actor.md#function-receivemsg) ([**u32**](classal_1_1_functor_v0_m.md) msg, [**HitSensor**](classal_1_1_hit_sensor.md) \* other, [**HitSensor**](classal_1_1_hit_sensor.md) \* me) <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**startClipped**](classal_1_1_live_actor.md#function-startclipped) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**updateCollider**](classal_1_1_live_actor.md#function-updatecollider) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v22**](classal_1_1_live_actor.md#function-v22) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v23**](classal_1_1_live_actor.md#function-v23) () <br> |


## Public Functions inherited from al::IUseNerve

See [al::IUseNerve](classal_1_1_i_use_nerve.md)

| Type | Name |
| ---: | :--- |
| virtual [**NerveKeeper**](classal_1_1_nerve_keeper.md) \* | [**getNerveKeeper**](classal_1_1_i_use_nerve.md#function-getnervekeeper) () const = 0<br> |


## Public Functions inherited from al::IUseEffectKeeper

See [al::IUseEffectKeeper](classal_1_1_i_use_effect_keeper.md)

| Type | Name |
| ---: | :--- |
| virtual [**EffectKeeper**](classal_1_1_effect_keeper.md) \* | [**getEffectKeeper**](classal_1_1_i_use_effect_keeper.md#function-geteffectkeeper) () const = 0<br> |


## Public Functions inherited from al::IUseAudioKeeper

See [al::IUseAudioKeeper](classal_1_1_i_use_audio_keeper.md)

| Type | Name |
| ---: | :--- |
| virtual [**AudioKeeper**](classal_1_1_audio_keeper.md) \* | [**getAudioKeeper**](classal_1_1_i_use_audio_keeper.md#function-getaudiokeeper) () const = 0<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v1**](classal_1_1_i_use_audio_keeper.md#function-v1) () <br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**v2**](classal_1_1_i_use_audio_keeper.md#function-v2) () <br> |


## Public Functions inherited from al::IUseStageSwitch

See [al::IUseStageSwitch](classal_1_1_i_use_stage_switch.md)

| Type | Name |
| ---: | :--- |
| virtual [**StageSwitchKeeper**](classal_1_1_stage_switch_keeper.md) \* | [**getStageSwitchKeeper**](classal_1_1_i_use_stage_switch.md#function-getstageswitchkeeper) () const = 0<br> |
| virtual [**void**](classal_1_1_functor_v0_m.md) | [**initStageSwitchKeeper**](classal_1_1_i_use_stage_switch.md#function-initstageswitchkeeper) () = 0<br> |








































## Protected Attributes inherited from al::LiveActor

See [al::LiveActor](classal_1_1_live_actor.md)

| Type | Name |
| ---: | :--- |
|  [**void**](classal_1_1_functor_v0_m.md) \* | [**\_4C**](classal_1_1_live_actor.md#variable-_4c)  <br> |
|  [**ActorActionKeeper**](classal_1_1_actor_action_keeper.md) \* | [**mActorActionKeeper**](classal_1_1_live_actor.md#variable-mactoractionkeeper)  <br> |
|  [**ActorExecuteInfo**](classal_1_1_actor_execute_info.md) \* | [**mActorExecuteInfo**](classal_1_1_live_actor.md#variable-mactorexecuteinfo)  <br> |
|  [**ActorLightCtrl**](classal_1_1_functor_v0_m.md) \* | [**mActorLightCtrl**](classal_1_1_live_actor.md#variable-mactorlightctrl)  <br> |
|  [**ActorPoseKeeperBase**](classal_1_1_actor_pose_keeper_base.md) \* | [**mActorPoseKeeper**](classal_1_1_live_actor.md#variable-mactorposekeeper)  <br> |
|  [**AudioKeeper**](classal_1_1_audio_keeper.md) \* | [**mAudioKeeper**](classal_1_1_live_actor.md#variable-maudiokeeper)  <br> |
|  [**Collider**](classal_1_1_collider.md) \* | [**mCollider**](classal_1_1_live_actor.md#variable-mcollider)  <br> |
|  [**CollisionParts**](classal_1_1_collision_parts.md) \* | [**mCollisionParts**](classal_1_1_live_actor.md#variable-mcollisionparts)  <br> |
|  [**EffectKeeper**](classal_1_1_effect_keeper.md) \* | [**mEffectKeeper**](classal_1_1_live_actor.md#variable-meffectkeeper)  <br> |
|  [**HitSensorKeeper**](classal_1_1_hit_sensor_keeper.md) \* | [**mHitSensorKeeper**](classal_1_1_live_actor.md#variable-mhitsensorkeeper)  <br> |
|  [**ModelKeeper**](classal_1_1_model_keeper.md) \* | [**mModelKeeper**](classal_1_1_live_actor.md#variable-mmodelkeeper)  <br> |
|  [**NerveKeeper**](classal_1_1_nerve_keeper.md) \* | [**mNerveKeeper**](classal_1_1_live_actor.md#variable-mnervekeeper)  <br> |
|  [**RailKeeper**](classal_1_1_rail_keeper.md) \* | [**mRailKeeper**](classal_1_1_live_actor.md#variable-mrailkeeper)  <br> |
|  [**ShadowKeeper**](classal_1_1_shadow_keeper.md) \* | [**mShadowKeeper**](classal_1_1_live_actor.md#variable-mshadowkeeper)  <br> |
|  [**StageSwitchKeeper**](classal_1_1_stage_switch_keeper.md) \* | [**mStageSwitchKeeper**](classal_1_1_live_actor.md#variable-mstageswitchkeeper)  <br> |
|  [**SubActorKeeper**](classal_1_1_sub_actor_keeper.md) \* | [**mSubActorKeeper**](classal_1_1_live_actor.md#variable-msubactorkeeper)  <br> |






















































































































## Public Functions Documentation




### function MapObjActor 

```C++
al::MapObjActor::MapObjActor (
    const sead::SafeString & name
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `/home/runner/work/RE-Pepper/RE-Pepper/lib/al/backup/include/MapObj/alMapObjActor.h`

