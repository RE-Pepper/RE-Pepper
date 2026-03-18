

# File alScene.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Scene**](dir_bbf0d395114b7d01e47e296975854f01.md) **>** [**alScene.h**](al_scene_8h.md)

[Go to the documentation of this file](al_scene_8h.md)


```C++
#pragma once

#include <Audio/alAudioKeeper.h>
#include <Nerve/alNerveExecutor.h>
#include <heap/seadHeap.h>

namespace al
{
class ActorFactory;
class ActorInitInfo;
class LayoutKit;
class LiveActorKit;
class SceneObjHolder;
class StageResourceKeeper;

class Scene : public NerveExecutor, public IUseAudioKeeper
{
private:
        AudioKeeper*         mAudioKeeper;
        LiveActorKit*        mLiveActorKit;
        LayoutKit*           mLayoutKit;
        SceneObjHolder*      mSceneObjHolder;
        ActorFactory*        mActorFactory;
        void*                _20;
        StageResourceKeeper* mResourceKeeper;
        void*                _28;
        void*                _2C;

        bool mIsAlive;

public:
        bool isAlive() const
        {
                return mIsAlive;
        }

        ActorFactory* getActorFactory() const
        {
                return mActorFactory;
        }

        void initAndLoadStageResource( const char* stageName, int scenario, sead::Heap* heap );
        void initSceneAudio( const char* stageName, int scenario, int, const sead::SafeString&, const char* userName );
        void initCameraDirector();
        void initActorFactory();
        void initSceneObjHolder();
        void initLiveActorKit();
        void initLayoutKit();

        void endInit( const ActorInitInfo& info );

public:
        virtual void appear();
        virtual void kill();
        virtual void init() = 0;
        virtual void movement();
        virtual void control();

        virtual void drawMainTop()
        {
        }

        virtual void drawSubTop()
        {
        }

        virtual void drawMainBottom()
        {
        }

        virtual void drawSubButtom()
        {
        }

        virtual void unk5()
        {
        }

        virtual void unk6()
        {
        }

        virtual void unk7()
        {
        }

        virtual AudioKeeper* getAudioKeeper() const; // probably not the right location

        virtual void unk8()
        {
        }

        virtual void draw3D()
        {
        }

        virtual void drawEffect()
        {
        }

public:
        Scene( const char* name );
};

static_assert( sizeof( Scene ) == 0x34, "" );

} // namespace al
```


