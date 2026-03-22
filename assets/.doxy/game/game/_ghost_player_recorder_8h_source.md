

# File GhostPlayerRecorder.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Player**](dir_c3d399ad73eabae4c9209488b7fe7035.md) **>** [**GhostPlayerRecorder.h**](_ghost_player_recorder_8h.md)

[Go to the documentation of this file](_ghost_player_recorder_8h.md)


```C++
#pragma once

#include <Scene/alISceneObj.h>
#include <math/seadVector.h>

class GhostPlayer;

class GhostPlayerRecorder : public al::ISceneObj
{
        friend class GhostPlayer;

private:
        struct Frame
        {
                sead::Vector3f mTrans;
                sead::Vector3f mRotate;
                int            _18;
                const char*    mActionName;
                int            _20;
        };

        Frame*       mFrames;
        GhostPlayer* mGhostPlayer;
        int          mNumFrames;
        int          mCurrentFrame;
        int          _14;
        int          _18;
        bool         _1C;
        bool         _1D;

public:
        void create( int numFrames );

        virtual const char* getSceneObjName() const
        {
                return "ゴーストプレイヤー記録";
        }

        virtual void initSceneObj();

        void initGhostPlayer( GhostPlayer* player )
        {
                mGhostPlayer = player;
        }

public:
        GhostPlayerRecorder();
};
```


