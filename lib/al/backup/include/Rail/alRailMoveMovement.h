#pragma once

#include <LiveActor/alLiveActor.h>
#include <Nerve/alHostStateBase.h>

namespace al
{

class RailMoveMovement : public HostStateBase<LiveActor>
{
private:
        float mSpeed;
        u32   mMoveType;

public:
        void exeMove();

public:
        RailMoveMovement( LiveActor* host, const ActorInitInfo& info, const char* speedParamName = "Arg0", const char* moveTypeParamName = "Arg1" );
};

} // namespace al
