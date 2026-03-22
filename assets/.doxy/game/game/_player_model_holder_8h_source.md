

# File PlayerModelHolder.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Player**](dir_c3d399ad73eabae4c9209488b7fe7035.md) **>** [**PlayerModelHolder.h**](_player_model_holder_8h.md)

[Go to the documentation of this file](_player_model_holder_8h.md)


```C++
#pragma once

#include <math/seadVector.h>

class PlayerFigureDirector;
struct PlayerActorInitInfo;
namespace al
{
struct ActorInitInfo;
}

class IUsePlayerModelChanger
{
public:
        virtual void change( const EPlayerFigure& figure );
};

class IUsePlayerModelShowHide
{
public:
        virtual void show();
        virtual void hide();
        virtual bool isHidden() const;
};

class IUsePlayerModelShadowShowHide
{
public:
        virtual void hideShadow();
        virtual void showShadow();
};

class IUsePlayerModelSilhouetteShowHide
{
public:
        virtual void showSilhouette();
        virtual void hideSilhouette();
        virtual bool isSilhouetteHidden() const;
};

class PlayerModel;

class PlayerModelHolder : public IUsePlayerModelChanger,
                          public IUsePlayerModelShowHide,
                          public IUsePlayerModelShadowShowHide,
                          public IUsePlayerModelSilhouetteShowHide
{
private:
        PlayerModel*  mModels[ 7 ];
        EPlayerFigure mCurrentFigure;
        bool          _30;
        bool          mIsHidden;
        bool          mIsShadowHidden;
        bool          mIsSilhouetteHidden;
        void*         _34[ 7 ];

public:
        static PlayerModel* createNormalPlayerModel( const al::ActorInitInfo& info,
                const PlayerActorInitInfo&                                    playerInfo,
                const sead::Vector3f*                                         transPtr,
                const sead::Vector3f*                                         rotatePtr,
                u64                                                           something );
        static PlayerModel* createMiniPlayerModel( const al::ActorInitInfo& info,
                const PlayerActorInitInfo&                                  playerInfo,
                const sead::Vector3f*                                       transPtr,
                const sead::Vector3f*                                       rotatePtr,
                u64                                                         something );
        static PlayerModel* createFirePlayerModel( const al::ActorInitInfo& info,
                const PlayerActorInitInfo&                                  playerInfo,
                const sead::Vector3f*                                       transPtr,
                const sead::Vector3f*                                       rotatePtr,
                u64                                                         something );
        // PlayerModelHolder::createRaccoonDogPlayerModel
        static PlayerModel* createBoomerangPlayerModel( const al::ActorInitInfo& info,
                const PlayerActorInitInfo&                                       playerInfo,
                const sead::Vector3f*                                            transPtr,
                const sead::Vector3f*                                            rotatePtr,
                u64                                                              something );
        // PlayerModelHolder::createRaccoonDogSpecialPlayerModel
        // PlayerModelHolder::createRaccoonDogWhitePlayerModel

public:
        virtual void change( const EPlayerFigure& figure );
        virtual void show();
        virtual void hide();
        virtual bool isHidden() const;
        virtual void showSilhouette();
        virtual void hideSilhouette();
        virtual bool isSilhouetteHidden() const;
        virtual void hideShadow();
        virtual void showShadow();

public:
        PlayerModelHolder( const al::ActorInitInfo& info, const PlayerActorInitInfo& playerInfo, const sead::Vector3f* transPtr, const sead::Vector3f* rotatePtr, u64 something );
};
```


