#include <KeyPose/alKeyPose.h>
#include <KeyPose/alKeyPoseKeeper.h>
#include <LiveActor/alActorInitInfo.h>
#include <Placement/alPlacementFunction.h>

namespace al
{

KeyPoseKeeper::KeyPoseKeeper()
    : mKeyPoses( nullptr ), mKeyPoseAmount( 0 ), mCurrentKeyPoseIdx( 0 ), mMoveTypeInt( 0 ), _10( true ),
      _11( false )
{
}

#ifdef NON_MATCHING

// puts size of KeyPose in r7 and does weird stuff
void KeyPoseKeeper::init( const ActorInitInfo& info )
{
        int linkChildNum = calcLinkChildNum( info );
        mKeyPoseAmount   = linkChildNum + 1;
        al::tryGetArg3( &mMoveTypeInt, info );
        mKeyPoses = new KeyPose[ mKeyPoseAmount ];
        mKeyPoses->init( getPlacementInfo( info ) );
        for ( int i = 0; i < mKeyPoseAmount - 1; i++ )
        {
                PlacementInfo keyPoseInfo;
                getLinksInfoByIndex( &keyPoseInfo, info, i );
                mKeyPoses[ i ].init( keyPoseInfo );
        }
}
#endif

const KeyPose* KeyPoseKeeper::getCurrentKeyPose() const
{
        return &mKeyPoses[ mCurrentKeyPoseIdx ];
}

#pragma no_inline

const KeyPose* KeyPoseKeeper::getNextKeyPose() const
{
        int idx;
        if ( _10 )
        {
                idx = mCurrentKeyPoseIdx + 1;
                if ( idx >= mKeyPoseAmount )
                        idx = 0;
        }
        else
        {
                idx = mCurrentKeyPoseIdx - 1;
                if ( idx < 0 )
                        idx = mKeyPoseAmount - 1;
        }
        return &mKeyPoses[ idx ];
}

#ifdef NON_MATCHING
// r4 not being pushed
const sead::Vector3f& getCurrentKeyTrans( const KeyPoseKeeper* p )
{
        return p->getCurrentKeyPose()->getTrans();
}
#endif

#ifdef NON_MATCHING
const sead::Vector3f& getNextKeyTrans( const KeyPoseKeeper* p )
{
        return p->getNextKeyPose()->getTrans();
}
#endif

#ifdef NON_MATCHING
const PlacementInfo* getNextKeyPlacementInfo( const KeyPoseKeeper* p )
{
        return p->getNextKeyPose()->getPlacementInfo();
}
#endif

} // namespace al
