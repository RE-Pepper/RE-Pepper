

# File alKeyPoseKeeper.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**KeyPose**](dir_c1df91a8d2930eb97f96869b778a7e0b.md) **>** [**alKeyPoseKeeper.h**](al_key_pose_keeper_8h.md)

[Go to the documentation of this file](al_key_pose_keeper_8h.md)


```C++
#pragma once

#include <Placement/alPlacementInfo.h>
#include <math/seadVector.h>

namespace al
{

class KeyPose;
class ActorInitInfo;

class KeyPoseKeeper
{
private:
        enum MoveType
        {
                MoveType_Loop,
                MoveType_Turn,
                MoveType_Stop,
                MoveType_Restart
        };

        KeyPose* mKeyPoses;
        int      mKeyPoseAmount;
        int      mCurrentKeyPoseIdx;

        union
        {
                int      mMoveTypeInt;
                MoveType mMoveType;
        };

        bool _10;
        bool _11;

public:
        void init( const ActorInitInfo& info );

        const KeyPose* getCurrentKeyPose() const;
        const KeyPose* getNextKeyPose() const;

public:
        KeyPoseKeeper();
};

const sead::Vector3f& getCurrentKeyTrans( const KeyPoseKeeper* p );
const sead::Vector3f& getNextKeyTrans( const KeyPoseKeeper* p );
const PlacementInfo*  getNextKeyPlacementInfo( const KeyPoseKeeper* p );

} // namespace al
```


