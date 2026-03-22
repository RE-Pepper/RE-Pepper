#pragma once

#include <math/seadMatrix.h>
#include <math/seadVector.h>

namespace al
{

void preScaleMtx( sead::Matrix34f* out, const sead::Vector3f& );
void calcMtxLocalTrans( sead::Vector3f* out, const sead::Matrix34f& mtx, const sead::Vector3f& trans );

} // namespace al
