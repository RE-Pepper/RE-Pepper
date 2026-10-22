#pragma once

#include <LiveActor/alLiveActor.h>
#include <Scene/alISceneObj.h>

namespace al
{
class SwitchKeepOnAreaGroup;
}

class SwitchOnAreaGroup;

class SwitchAreaDirector : public al::LiveActor, public al::ISceneObj
{
private:
        SwitchOnAreaGroup*           mSwitchOnAreaGroup;
        al::SwitchKeepOnAreaGroup*    mSwitchKeepOnAreaGroup;

public:
        virtual void movement();
        virtual void unk1();

public:
        SwitchAreaDirector();
};
