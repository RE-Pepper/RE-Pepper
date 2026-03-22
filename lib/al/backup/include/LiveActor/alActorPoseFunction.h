#pragma once

#include <LiveActor/alActorPoseKeeper.h>
#include <LiveActor/alLiveActor.h>
#include <math/seadMatrix.h>

class alActorPoseFunction
{
public:
        static void calcBaseMtx( sead::Matrix34f* out, const al::LiveActor* actor )
        {
                actor->mActorPoseKeeper->calcBaseMtx( out );
        }
};
