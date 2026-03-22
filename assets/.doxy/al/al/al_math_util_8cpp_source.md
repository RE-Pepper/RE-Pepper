

# File alMathUtil.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Math**](dir_a966ac3a74b4b7a5925df4209ce9b3f1.md) **>** [**alMathUtil.cpp**](al_math_util_8cpp.md)

[Go to the documentation of this file](al_math_util_8cpp.md)


```C++
#include <Math/alMathUtil.h>

namespace al
{

bool isNearZero( float value, float range )
{
        return ( value < 0 ? -value : value ) < range;
}

} // namespace al
```


