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
