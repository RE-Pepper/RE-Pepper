#pragma once

#include <KeyPose/alKeyPose.h>
#include <Placement/alPlacementFunction.h>

namespace al
{

KeyPose::KeyPose()
    : mQuat( sead::Quatf::unit ), mTrans( sead::Vector3f::zero ), mPlacementInfo( nullptr ), _20( 0.0 )
{
}

void KeyPose::init( const PlacementInfo& info )
{
        tryGetQuat( &mQuat, info );
        tryGetTrans( &mTrans, info );
        mPlacementInfo = new PlacementInfo( info );
}

} // namespace al
