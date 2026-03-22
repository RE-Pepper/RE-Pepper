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
