

# File alAreaShapeCube.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**AreaObj**](dir_b7fc9200a4f7d26d4acf4ee56ee313c7.md) **>** [**alAreaShapeCube.h**](al_area_shape_cube_8h.md)

[Go to the documentation of this file](al_area_shape_cube_8h.md)


```C++
#pragma once

#include <AreaObj/alAreaShape.h>

namespace al
{

class AreaShapeCube : public AreaShape
{
private:
        bool mIsCubeBase;

public:
        virtual bool isInVolume( const sead::Vector3f& trans ) const;
        // virtual void v2();
public:
        AreaShapeCube( bool isCubeBase );
};

} // namespace al
```


