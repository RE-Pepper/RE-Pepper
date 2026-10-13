#include "Player/PlayerFunction.h"

#include <LiveActor/alActorPoseKeeper.h>
#include <System/Application.h>

#include "Player/PlayerActor.h"

namespace rp
{

#pragma no_inline
#ifdef NON_MATCHING

// linker shenanigans
PlayerActor* getPlayerActor()
{
        return Application::instance()->getPlayerActor();
}

const sead::Vector3f& getPlayerPos()
{
        return al::getTrans( getPlayerActor() );
}
#endif

} // namespace rp
