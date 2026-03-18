

# File alQuatUtil.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Math**](dir_93118792663f6968a18c175a87f86283.md) **>** [**alQuatUtil.h**](al_quat_util_8h.md)

[Go to the documentation of this file](al_quat_util_8h.md)


```C++
#pragma once

#include <math/seadQuat.h>

namespace al
{

void rotateQuatXDirDegree( sead::Quatf* out, const sead::Quatf& from, float degrees );
void rotateQuatYDirDegree( sead::Quatf* out, const sead::Quatf& from, float degrees );
void rotateQuatZDirDegree( sead::Quatf* out, const sead::Quatf& from, float degrees );

void calcQuatSide( sead::Vector3f* out, const sead::Quatf& from );

} // namespace al
```


