

# File alAreaShapeCube.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**AreaObj**](dir_65406aa8482a23b720984def0cee3032.md) **>** [**alAreaShapeCube.h**](al_area_shape_cube_8h.md)

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


