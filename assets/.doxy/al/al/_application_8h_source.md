

# File Application.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**System**](dir_29a5069bbf312f731d8cb4e203fae6bc.md) **>** [**Application.h**](_application_8h.md)

[Go to the documentation of this file](_application_8h.md)


```C++
#pragma once

#include <heap/seadDisposer.h>

namespace al
{
class EffectUserInfo;
class GameFrameworkCtr;
class LiveActorKit;
class MapObjActor;
class SceneObjHolder;
class SystemKit;
} // namespace al
class PlayerActor;
class RootTask;

class Application
{
        SEAD_SINGLETON_DISPOSER( Application )
        friend class ApplicationFunction;

private:
        void*                 _10;
        al::GameFrameworkCtr* mGameFramework;
        al::SystemKit*        mSystemKit;
        u8                    _1C[ 24 ];
        u8                    _34[ 24 ];
        void*                 _4C;
        al::SceneObjHolder*   mSceneObjHolder;
        al::LiveActorKit*     mLiveActorKit;
        void*                 mEffectUserInfo;
        PlayerActor*          mPlayerActor;

public:
        al::SceneObjHolder* getSceneObjHolder() const
        {
                return mSceneObjHolder;
        }

        void setSceneObjHolder( al::SceneObjHolder* holder )
        {
                mSceneObjHolder = holder;
        }

        al::LiveActorKit* getLiveActorKit() const
        {
                return mLiveActorKit;
        }

        void setLiveActorKit( al::LiveActorKit* holder )
        {
                mLiveActorKit = holder;
        }

        al::SystemKit* getSystemKit() const
        {
                return mSystemKit;
        }

        PlayerActor* getPlayerActor() const
        {
                return mPlayerActor;
        }

        RootTask* getRootTask() const;

public:
        void init();
        void run();
};

static_assert( sizeof( Application ) == 0x60, "" );

namespace al
{

Application* getApplication();

} // namespace al
```


