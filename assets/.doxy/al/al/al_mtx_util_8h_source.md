

# File alMtxUtil.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Math**](dir_93118792663f6968a18c175a87f86283.md) **>** [**alMtxUtil.h**](al_mtx_util_8h.md)

[Go to the documentation of this file](al_mtx_util_8h.md)


```C++
#pragma once

#include <math/seadMatrix.h>
#include <math/seadVector.h>

namespace al
{

void preScaleMtx( sead::Matrix34f* out, const sead::Vector3f& );
void calcMtxLocalTrans( sead::Vector3f* out, const sead::Matrix34f& mtx, const sead::Vector3f& trans );

} // namespace al
```


