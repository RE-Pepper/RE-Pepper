

# File alCollider.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Collision**](dir_b64277db147a0cb833174dd0bf4617cc.md) **>** [**alCollider.h**](al_collider_8h.md)

[Go to the documentation of this file](al_collider_8h.md)


```C++
#pragma once

namespace al
{

class Collider
{
private:
        u8    _0[ 0xc0 ];
        float mGroundDistance;

public:
        float getGroundDistance()
        {
                return mGroundDistance;
        }

        void onInvalidate();
};

} // namespace al
```


