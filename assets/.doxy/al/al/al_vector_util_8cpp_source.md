

# File alVectorUtil.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Math**](dir_17d2d8808d20549c6aef9df204bad76e.md) **>** [**alVectorUtil.cpp**](al_vector_util_8cpp.md)

[Go to the documentation of this file](al_vector_util_8cpp.md)


```C++
#include <Math/alVectorUtil.h>

namespace al
{

void lerpVec( sead::Vector3f* out, const sead::Vector3f& from, const sead::Vector3f& to, float amount )
{
        out->x = from.x + ( to.x - from.x ) * amount;
        out->y = from.y + ( to.y - from.y ) * amount;
        out->z = from.z + ( to.z - from.z ) * amount;
}

} // namespace al
```


