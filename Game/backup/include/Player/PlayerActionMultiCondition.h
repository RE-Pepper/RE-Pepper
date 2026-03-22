#pragma once

#include <container/seadOffsetList.h>

#include "Player/PlayerActionCondition.h"

class PlayerActionMultiCondition : public PlayerActionCondition
{
private:
        sead::OffsetList<PlayerActionCondition*> mConditions;

public:
        void append( PlayerActionCondition* condition );

public:
        virtual bool check();
        virtual void setup();

public:
        PlayerActionMultiCondition();
};
