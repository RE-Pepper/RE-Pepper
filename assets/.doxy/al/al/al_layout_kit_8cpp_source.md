

# File alLayoutKit.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Layout**](dir_17ff0a3ba0f744361034893725301bda.md) **>** [**alLayoutKit.cpp**](al_layout_kit_8cpp.md)

[Go to the documentation of this file](al_layout_kit_8cpp.md)


```C++
#include <Execute/alExecuteDirector.h>
#include <Layout/alLayoutKit.h>

namespace al
{

LayoutKit::LayoutKit( FontHolder* fontHolder )
    : _0( nullptr ), mFontHolder( fontHolder ), mExecuteDirector( nullptr ), _C( nullptr ), _10( nullptr ),
      _14( nullptr )
{
}

void LayoutKit::createExecuteDirector( int p )
{
        mExecuteDirector      = new ExecuteDirector( p );
        mExecuteDirector->_18 = _14;
        mExecuteDirector->init();
}

} // namespace al
```


