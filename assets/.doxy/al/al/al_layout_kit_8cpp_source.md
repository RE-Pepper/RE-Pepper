

# File alLayoutKit.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Layout**](dir_1957e6da08be5c5351242f28ef490eb7.md) **>** [**alLayoutKit.cpp**](al_layout_kit_8cpp.md)

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


