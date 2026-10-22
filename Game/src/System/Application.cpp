#include "System/Application.h"

#ifdef NON_MATCHING
Application::Application()
{
}

SEAD_SINGLETON_DISPOSER_IMPL( Application )

Application* al::getApplication()
{
        return Application::instance();
}
#endif
