#pragma once

#include <math/seadVector.h>

namespace al
{

void lerpVec( sead::Vector3f* out, const sead::Vector3f& from, const sead::Vector3f& to, float amount );

} // namespace al
