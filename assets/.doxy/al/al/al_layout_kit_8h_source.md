

# File alLayoutKit.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Layout**](dir_71ac96d9eee999c5231127773bfe6eda.md) **>** [**alLayoutKit.h**](al_layout_kit_8h.md)

[Go to the documentation of this file](al_layout_kit_8h.md)


```C++
#pragma once

namespace al
{
class ExecuteDirector;
class FontHolder;

class LayoutKit
{
private:
        void*            _0;
        FontHolder*      mFontHolder;
        ExecuteDirector* mExecuteDirector;
        void*            _C;
        void*            _10;
        void*            _14;

public:
        void createExecuteDirector( int p );
        void createEffectSystem();
        void update();

public:
        LayoutKit( FontHolder* fontHolder );
};

} // namespace al
```


