#pragma once

#include <math/seadVector.h>

class PlayerActor;

namespace rp
{

PlayerActor*          getPlayerActor();
const sead::Vector3f& getPlayerPos();

} // namespace rp
