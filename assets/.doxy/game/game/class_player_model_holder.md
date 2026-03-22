

# Class PlayerModelHolder



[**ClassList**](annotated.md) **>** [**PlayerModelHolder**](class_player_model_holder.md)





* `#include <PlayerModelHolder.h>`



Inherits the following classes: [IUsePlayerModelChanger](class_i_use_player_model_changer.md),  [IUsePlayerModelShowHide](class_i_use_player_model_show_hide.md),  [IUsePlayerModelShadowShowHide](class_i_use_player_model_shadow_show_hide.md),  [IUsePlayerModelSilhouetteShowHide](class_i_use_player_model_silhouette_show_hide.md)


















































































































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**PlayerModelHolder**](#function-playermodelholder) (const al::ActorInitInfo & info, const [**PlayerActorInitInfo**](class_player_actor_init_info.md) & playerInfo, const sead::Vector3f \* transPtr, const sead::Vector3f \* rotatePtr, u64 something) <br> |
| virtual void | [**change**](#function-change) (const [**EPlayerFigure**](_player_figure_director_8h.md#enum-eplayerfigure) & figure) <br> |
| virtual void | [**hide**](#function-hide) () <br> |
| virtual void | [**hideShadow**](#function-hideshadow) () <br> |
| virtual void | [**hideSilhouette**](#function-hidesilhouette) () <br> |
| virtual bool | [**isHidden**](#function-ishidden) () const<br> |
| virtual bool | [**isSilhouetteHidden**](#function-issilhouettehidden) () const<br> |
| virtual void | [**show**](#function-show) () <br> |
| virtual void | [**showShadow**](#function-showshadow) () <br> |
| virtual void | [**showSilhouette**](#function-showsilhouette) () <br> |


## Public Functions inherited from IUsePlayerModelChanger

See [IUsePlayerModelChanger](class_i_use_player_model_changer.md)

| Type | Name |
| ---: | :--- |
| virtual void | [**change**](class_i_use_player_model_changer.md#function-change) (const [**EPlayerFigure**](_player_figure_director_8h.md#enum-eplayerfigure) & figure) <br> |


## Public Functions inherited from IUsePlayerModelShowHide

See [IUsePlayerModelShowHide](class_i_use_player_model_show_hide.md)

| Type | Name |
| ---: | :--- |
| virtual void | [**hide**](class_i_use_player_model_show_hide.md#function-hide) () <br> |
| virtual bool | [**isHidden**](class_i_use_player_model_show_hide.md#function-ishidden) () const<br> |
| virtual void | [**show**](class_i_use_player_model_show_hide.md#function-show) () <br> |


## Public Functions inherited from IUsePlayerModelShadowShowHide

See [IUsePlayerModelShadowShowHide](class_i_use_player_model_shadow_show_hide.md)

| Type | Name |
| ---: | :--- |
| virtual void | [**hideShadow**](class_i_use_player_model_shadow_show_hide.md#function-hideshadow) () <br> |
| virtual void | [**showShadow**](class_i_use_player_model_shadow_show_hide.md#function-showshadow) () <br> |


## Public Functions inherited from IUsePlayerModelSilhouetteShowHide

See [IUsePlayerModelSilhouetteShowHide](class_i_use_player_model_silhouette_show_hide.md)

| Type | Name |
| ---: | :--- |
| virtual void | [**hideSilhouette**](class_i_use_player_model_silhouette_show_hide.md#function-hidesilhouette) () <br> |
| virtual bool | [**isSilhouetteHidden**](class_i_use_player_model_silhouette_show_hide.md#function-issilhouettehidden) () const<br> |
| virtual void | [**showSilhouette**](class_i_use_player_model_silhouette_show_hide.md#function-showsilhouette) () <br> |


## Public Static Functions

| Type | Name |
| ---: | :--- |
|  PlayerModel \* | [**createBoomerangPlayerModel**](#function-createboomerangplayermodel) (const al::ActorInitInfo & info, const [**PlayerActorInitInfo**](class_player_actor_init_info.md) & playerInfo, const sead::Vector3f \* transPtr, const sead::Vector3f \* rotatePtr, u64 something) <br> |
|  PlayerModel \* | [**createFirePlayerModel**](#function-createfireplayermodel) (const al::ActorInitInfo & info, const [**PlayerActorInitInfo**](class_player_actor_init_info.md) & playerInfo, const sead::Vector3f \* transPtr, const sead::Vector3f \* rotatePtr, u64 something) <br> |
|  PlayerModel \* | [**createMiniPlayerModel**](#function-createminiplayermodel) (const al::ActorInitInfo & info, const [**PlayerActorInitInfo**](class_player_actor_init_info.md) & playerInfo, const sead::Vector3f \* transPtr, const sead::Vector3f \* rotatePtr, u64 something) <br> |
|  PlayerModel \* | [**createNormalPlayerModel**](#function-createnormalplayermodel) (const al::ActorInitInfo & info, const [**PlayerActorInitInfo**](class_player_actor_init_info.md) & playerInfo, const sead::Vector3f \* transPtr, const sead::Vector3f \* rotatePtr, u64 something) <br> |


































































































































## Public Functions Documentation




### function PlayerModelHolder 

```C++
PlayerModelHolder::PlayerModelHolder (
    const al::ActorInitInfo & info,
    const PlayerActorInitInfo & playerInfo,
    const sead::Vector3f * transPtr,
    const sead::Vector3f * rotatePtr,
    u64 something
) 
```




<hr>



### function change 

```C++
virtual void PlayerModelHolder::change (
    const EPlayerFigure & figure
) 
```



Implements [*IUsePlayerModelChanger::change*](class_i_use_player_model_changer.md#function-change)


<hr>



### function hide 

```C++
virtual void PlayerModelHolder::hide () 
```



Implements [*IUsePlayerModelShowHide::hide*](class_i_use_player_model_show_hide.md#function-hide)


<hr>



### function hideShadow 

```C++
virtual void PlayerModelHolder::hideShadow () 
```



Implements [*IUsePlayerModelShadowShowHide::hideShadow*](class_i_use_player_model_shadow_show_hide.md#function-hideshadow)


<hr>



### function hideSilhouette 

```C++
virtual void PlayerModelHolder::hideSilhouette () 
```



Implements [*IUsePlayerModelSilhouetteShowHide::hideSilhouette*](class_i_use_player_model_silhouette_show_hide.md#function-hidesilhouette)


<hr>



### function isHidden 

```C++
virtual bool PlayerModelHolder::isHidden () const
```



Implements [*IUsePlayerModelShowHide::isHidden*](class_i_use_player_model_show_hide.md#function-ishidden)


<hr>



### function isSilhouetteHidden 

```C++
virtual bool PlayerModelHolder::isSilhouetteHidden () const
```



Implements [*IUsePlayerModelSilhouetteShowHide::isSilhouetteHidden*](class_i_use_player_model_silhouette_show_hide.md#function-issilhouettehidden)


<hr>



### function show 

```C++
virtual void PlayerModelHolder::show () 
```



Implements [*IUsePlayerModelShowHide::show*](class_i_use_player_model_show_hide.md#function-show)


<hr>



### function showShadow 

```C++
virtual void PlayerModelHolder::showShadow () 
```



Implements [*IUsePlayerModelShadowShowHide::showShadow*](class_i_use_player_model_shadow_show_hide.md#function-showshadow)


<hr>



### function showSilhouette 

```C++
virtual void PlayerModelHolder::showSilhouette () 
```



Implements [*IUsePlayerModelSilhouetteShowHide::showSilhouette*](class_i_use_player_model_silhouette_show_hide.md#function-showsilhouette)


<hr>
## Public Static Functions Documentation




### function createBoomerangPlayerModel 

```C++
static PlayerModel * PlayerModelHolder::createBoomerangPlayerModel (
    const al::ActorInitInfo & info,
    const PlayerActorInitInfo & playerInfo,
    const sead::Vector3f * transPtr,
    const sead::Vector3f * rotatePtr,
    u64 something
) 
```




<hr>



### function createFirePlayerModel 

```C++
static PlayerModel * PlayerModelHolder::createFirePlayerModel (
    const al::ActorInitInfo & info,
    const PlayerActorInitInfo & playerInfo,
    const sead::Vector3f * transPtr,
    const sead::Vector3f * rotatePtr,
    u64 something
) 
```




<hr>



### function createMiniPlayerModel 

```C++
static PlayerModel * PlayerModelHolder::createMiniPlayerModel (
    const al::ActorInitInfo & info,
    const PlayerActorInitInfo & playerInfo,
    const sead::Vector3f * transPtr,
    const sead::Vector3f * rotatePtr,
    u64 something
) 
```




<hr>



### function createNormalPlayerModel 

```C++
static PlayerModel * PlayerModelHolder::createNormalPlayerModel (
    const al::ActorInitInfo & info,
    const PlayerActorInitInfo & playerInfo,
    const sead::Vector3f * transPtr,
    const sead::Vector3f * rotatePtr,
    u64 something
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `Game/backup/include/Player/PlayerModelHolder.h`

