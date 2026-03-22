

# File alAreaShape.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**AreaObj**](dir_b7fc9200a4f7d26d4acf4ee56ee313c7.md) **>** [**alAreaShape.h**](al_area_shape_8h.md)

[Go to the documentation of this file](al_area_shape_8h.md)


```C++
#pragma once

#include <math/seadMatrix.h>
#include <math/seadVector.h>

namespace al
{

class AreaShape
{
private:
        const sead::Matrix34f* mBaseMtxPtr;
        sead::Vector3f         mScale;

public:
        bool calcLocalPos( sead::Vector3f* out, const sead::Vector3f& trans ) const;

        void setBaseMtxPtr( const sead::Matrix34f* baseMtxPtr )
        {
                mBaseMtxPtr = baseMtxPtr;
        }

        void setScale( const sead::Vector3f& scale );

public:
        virtual bool isInVolume( const sead::Vector3f& trans ) const = 0;
        virtual void v1()                                            = 0;
        virtual void v2()                                            = 0;

public:
        AreaShape();
};

} // namespace al
```


