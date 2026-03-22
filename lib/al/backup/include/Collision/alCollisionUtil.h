#pragma once

#include <math/seadMatrix.h>

namespace al
{
class LiveActor;

void syncCollisionMtx( LiveActor* actor, const sead::Matrix34f* );

bool isCollided( const LiveActor* actor );
bool isCollidedGround( const LiveActor* actor );
bool isCollidedWall( const LiveActor* actor );
bool isOnGround( const LiveActor* actor, u32 );

} // namespace al
