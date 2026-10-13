#include "Player/PlayerAnimator.h"

#include "Player/PlayerAnimFrameCtrl.h"

float PlayerAnimator::getAnimFrame() const
{
        return mAnimFrameCtrl->getCurrentFrame();
}
