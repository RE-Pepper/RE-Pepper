#pragma once

#include "Player/PlayerActionMultiCondition.h"

class IUsePlayerAnimator;

class PlayerActionConditionAnimEnd : public PlayerActionCondition
{
private:
        const char*         mAnimName;
        IUsePlayerAnimator* mUsePlayerAnimator;
        int                 mAnimEndFrame;

public:
        virtual bool check();

public:
        PlayerActionConditionAnimEnd( IUsePlayerAnimator* animator, const char* animName, int animEndFrame );
};
