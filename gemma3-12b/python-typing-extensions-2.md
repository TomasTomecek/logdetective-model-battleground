The package foo failed to build, here is a possible explanation why.

Please know that the explanation was provided by AI and may be incorrect.
In this case, we are 95.31% certain of the response :slight_smile:.

The build of the `python-typing-extensions` package (version 4.13.2) failed during the check phase. The root cause appears to be a series of failing tests within the package's test suite, specifically related to TypedDict functionality and annotations. The tests `test_stock_annotations`, `test_extra_items_class_arg`, `test_implicit_any_inheritance`, `test_regular_extra_items_legacy`, and `test_total` all failed, resulting in 20 failures and 12 errors overall. These failures suggest inconsistencies in how the package handles type annotations, particularly within `TypedDict` definitions and inheritance. The `AssertionError` messages highlight discrepancies in expected versus actual sets of keys and annotations.  The final failure was triggered by a bad exit status from the `%check` script during the RPM build process, which itself resulted from the failed tests. The systemd-nspawn command used within the mock build environment ultimately failed to complete, leading to a "Copr build error: Build failed."

A possible solution would be to investigate and fix the failing tests in the `python-typing-extensions` package. This would involve examining the code in `src/test_typing_extensions.py` around lines 4497, 4921, and 4988 to understand why the assertions are failing and adjust the code or test expectations accordingly. It's also possible that the test environment or configuration is the cause, so verifying that the test setup is consistent and correctly reflects the intended behavior would be worthwhile.


<details>
<ul>

<li>
<b>Line 5:</b> <code>INFO: Reading stdout from command: md5sum typing_extensions-4.13.2.tar.gz

</code>
The RPM build process executed the command `md5sum typing_extensions-4.13.2.tar.gz` and captured its standard output. The captured output is being presented as informational ("INFO").

</li>

<li>
<b>Line 24:</b> <code>Start: clean chroot
</code>
The RPM build process initiated a "clean chroot" operation. This signifies the beginning of a stage where the build environment's chroot is being prepared or cleared.
</li>

<li>
<b>Line 25:</b> <code>Finish: clean chroot
</code>
The RPM build log snippet indicates the completion of the "clean chroot" phase of the build process. This phase removes files from the build environment's chroot.

</li>

<li>
<b>Line 971:</b> <code>/bin/tar: Removing leading `/' from member names
</code>
The snippet indicates the `tar` command, used during the RPM build process, removed leading forward slashes (`/`) from member names within an archive. This is a standard `tar` behavior to ensure portability and avoid absolute paths within the archive.
</li>

<li>
<b>Line 1447:</b> <code>======================================================================
</code>
The snippet displays a line containing a string of equal signs, indicating a section divider or header in an RPM build log. The string is visually formatted for clarity and likely separates different stages or components of the build process.

</li>

<li>
<b>Line 1449:</b> <code>----------------------------------------------------------------------
</code>
The snippet presents a string containing a line of dashes, likely a separator or header in an RPM build log. It indicates a demarcation point within the log file.

</li>

<li>
<b>Line 1651:</b> <code>FAIL: test_stock_annotations (test_typing_extensions.TestGetAnnotations.test_stock_annotations)
</code>
The build log indicates a test failure. Specifically, the test `test_stock_annotations` within the `test_typing_extensions.TestGetAnnotations` test suite failed.
</li>

<li>
<b>Line 1704:</b> <code>AssertionError: Items in the second set but not the first:
'a'

</code>
The build process encountered an `AssertionError`. The error message indicates the presence of the element 'a' in the second set being compared, but not in the first.
</li>

<li>
<b>Line 1710:</b> <code>Traceback (most recent call last):
  File "/builddir/build/BUILD/python-typing-extensions-4.13.2-build/typing_extensions-4.13.2/src/test_typing_extensions.py", line 4988, in test_closed_inheritance
    self.assertEqual(Base.__required_keys__, frozenset({"a"}))
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code>
The build log indicates a test failure within the `python-typing-extensions` package (version 4.13.2). Specifically, the test `test_closed_inheritance` in the file `src/test_typing_extensions.py` failed on line 4988. The assertion `self.assertEqual(Base.__required_keys__, frozenset({"a"}))` did not pass.

</li>

<li>
<b>Line 1731:</b> <code>Traceback (most recent call last):
  File "/builddir/build/BUILD/python-typing-extensions-4.13.2-build/typing_extensions-4.13.2/src/test_typing_extensions.py", line 4497, in test_extra_items_class_arg
    self.assertEqual(TD.__annotations__, {'a': str})
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code>
The build log indicates a test failure within the `python-typing-extensions` package (version 4.13.2). Specifically, the test `test_extra_items_class_arg` in the file `src/test_typing_extensions.py` failed on line 4497 due to an assertion error (`self.assertEqual`). The assertion compared `TD.__annotations__` to `{'a': str}` and found them unequal.

</li>

<li>
<b>Line 1767:</b> <code>FAIL: test_implicit_any_inheritance (test_typing_extensions.TypedDictTests.test_implicit_any_inheritance)
</code>
The build log indicates a test failure. Specifically, the test `test_implicit_any_inheritance` within the `TypedDictTests` class of the `test_typing_extensions` test suite failed.
</li>

<li>
<b>Line 1831:</b> <code>+ {'label': <class 'str'>, 'x': <class 'int'>, 'y': <class 'int'>}

</code>
The RPM build log snippet shows a tuple containing an integer (1831) and a dictionary. The dictionary has three keys: 'label' (value is a string), 'x' (value is an integer), and 'y' (value is an integer). This appears to be data being logged during the build process.

</li>

<li>
<b>Line 1844:</b> <code>FAIL: test_regular_extra_items_legacy (test_typing_extensions.TypedDictTests.test_regular_extra_items_legacy)
</code>
The build log indicates a test failure. Specifically, the test `test_regular_extra_items_legacy` within the `test_typing_extensions.TypedDictTests` test suite failed.

</li>

<li>
<b>Line 1846:</b> <code>Traceback (most recent call last):
  File "/builddir/build/BUILD/python-typing-extensions-4.13.2-build/typing_extensions-4.13.2/src/test_typing_extensions.py", line 4921, in test_regular_extra_items_legacy
    self.assertEqual(ExtraReadOnly.__required_keys__, frozenset({'__extra_items__'}))
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code>
The build log snippet indicates a `Traceback` originating from `/builddir/build/BUILD/python-typing-extensions-4.13.2-build/typing_extensions-4.13.2/src/test_typing_extensions.py`. Specifically, the error occurred on line 4921 within the test function `test_regular_extra_items_legacy`. The traceback shows an assertion failure: `self.assertEqual(ExtraReadOnly.__required_keys__, frozenset({'__extra_items__'}))`.

</li>

<li>
<b>Line 1850:</b> <code>AssertionError: Items in the second set but not the first:
'__extra_items__'

</code>
The RPM build process encountered an `AssertionError`. The error message indicates the presence of items in a second set that are not found in a first set, specifically identifying `'__extra_items__'` as the differing item.
</li>

<li>
<b>Line 1866:</b> <code>FAIL: test_total (test_typing_extensions.TypedDictTests.test_total)
</code>
The build log snippet indicates a test failure. Specifically, the test `test_total` within the `test_typing_extensions.TypedDictTests` suite failed. The failure is represented by the string "FAIL: test_total (test_typing_extensions.TypedDictTests.test_total)".

</li>

<li>
<b>Line 1872:</b> <code>AssertionError: frozenset() != {'log_path', 'log_level'}

</code>
The RPM build process encountered an `AssertionError` during a test or script execution. The error message indicates that a `frozenset()` was compared to the set `{'log_path', 'log_level'}` and the comparison failed.

</li>

<li>
<b>Line 1875:</b> <code>Ran 517 tests in 0.209s

</code>
The build log indicates the execution of 517 tests, which completed in 0.209 seconds.
</li>

<li>
<b>Line 1877:</b> <code>FAILED (failures=20, errors=12, skipped=15)

</code>
The RPM build process failed. It encountered 20 failures, 12 errors, and 15 skipped tests.
</li>

<li>
<b>Line 1879:</b> <code>RPM build errors:
error: Bad exit status from /var/tmp/rpm-tmp.5QvbcS (%check)
    Bad exit status from /var/tmp/rpm-tmp.5QvbcS (%check)
</code>
The RPM build process encountered an error. Specifically, the `%check` script located at `/var/tmp/rpm-tmp.5QvbcS` exited with a non-zero status, indicating a failure. This is reported as "Bad exit status."
</li>

<li>
<b>Line 1882:</b> <code>Finish: rpmbuild python-typing-extensions-4.13.2-1.fc43.src.rpm
</code>
The RPM build process completed successfully for the package `python-typing-extensions`, version `4.13.2-1.fc43`, using the source RPM file `python-typing-extensions-4.13.2-1.fc43.src.rpm`.

</li>

<li>
<b>Line 1883:</b> <code>Finish: build phase for python-typing-extensions-4.13.2-1.fc43.src.rpm
</code>
The snippet indicates the completion of the build phase for the RPM package `python-typing-extensions-4.13.2-1.fc43.src.rpm`. The build process, specifically the build phase, has finished.

</li>

<li>
<b>Line 1888:</b> <code>ERROR: Exception(/var/lib/copr-rpmbuild/results/python-typing-extensions-4.13.2-1.fc43.src.rpm) Config(fedora-rawhide-x86_64) 0 minutes 20 seconds
</code>
The RPM build process encountered an error during the build of `python-typing-extensions-4.13.2-1.fc43.src.rpm` while building for the `fedora-rawhide-x86_64` architecture. The error was an exception, and the build took 20 seconds. The error message is stored in a string.

</li>

<li>
<b>Line 1894:</b> <code>ERROR: Command failed: 
 # /usr/bin/systemd-nspawn -q -M c119e3a095794ef1ad625ab455397584 -D /var/lib/mock/fedora-rawhide-x86_64-1747040968.970771/root -a -u mockbuild --capability=cap_ipc_lock --rlimit=RLIMIT_NOFILE=10240 --capability=cap_ipc_lock --bind=/tmp/mock-resolv.tshlrkhz:/etc/resolv.conf --bind=/dev/btrfs-control --bind=/dev/mapper/control --bind=/dev/fuse --bind=/dev/loop-control --bind=/dev/loop0 --bind=/dev/loop1 --bind=/dev/loop2 --bind=/dev/loop3 --bind=/dev/loop4 --bind=/dev/loop5 --bind=/dev/loop6 --bind=/dev/loop7 --bind=/dev/loop8 --bind=/dev/loop9 --bind=/dev/loop10 --bind=/dev/loop11 --console=pipe --setenv=TERM=vt100 --setenv=SHELL=/bin/bash --setenv=HOME=/builddir --setenv=HOSTNAME=mock --setenv=PATH=/usr/bin:/bin:/usr/sbin:/sbin '--setenv=PROMPT_COMMAND=printf "\033]0;<mock-chroot>\007"' '--setenv=PS1=<mock-chroot> \s-\v\$ ' --setenv=LANG=C.UTF-8 --resolv-conf=off bash --login -c '/usr/bin/rpmbuild -ba --noprep  --target x86_64 /builddir/build/originals/python-typing-extensions.spec'

</code>
The build log indicates a failure during a systemd-nspawn command executed within a mock build environment. The command attempted to run `rpmbuild -ba --noprep --target x86_64 /builddir/build/originals/python-typing-extensions.spec` inside a chroot environment. The command failed with an error; the specific reason for the failure is not provided within this snippet. The command included several bind mounts, capability assignments, resource limits, and environment variable settings for the chroot.

</li>

<li>
<b>Line 1897:</b> <code>Copr build error: Build failed
</code>
The RPM build process encountered an error labeled "Copr build error: Build failed." The error occurred at step 1897 of the build process.

</li>

</ul>
</details>

<details>
  <summary>Logs</summary>
  <p>
    Log Detective analyzed the following logs files to provide an explanation:
  </p>

  <ul>
    <li><a href="https://download.copr.fedorainfracloud.org/results/@python/python3.14-b1/fedora-rawhide-x86_64/09020507-python-typing-extensions/builder-live.log.gz">https://download.copr.fedorainfracloud.org/results/@python/python3.14-b1/fedora-rawhide-x86_64/09020507-python-typing-extensions/builder-live.log.gz</a></li>
  </ul>

  <p>
    Additional logs are available from:
    <ul>
    <li><a href="https://gitlab.foobar.baz//-/jobs/1/artifacts/download">artifacts.zip</a></li>
  </ul>
  </p>

  <p>
    Please know that these log files are automatically removed after some
    time, so you might need a backup.
  </p>
</details>

<details>
  <summary>Help</summary>
  <p>Don't hesitate to reach out.</p>

  <ul>
    <li><a href="https://github.com/fedora-copr/logdetective">Upstream</a></li>
    <li><a href="https://github.com/fedora-copr/logdetective/issues">Issue tracker</a></li>
    <li><a href="https://redhat.enterprise.slack.com/archives/C06DWNVKKDE">Slack</a></li>
    <li><a href="https://log-detective.com/documentation">Documentation</a></li>
  </ul>
</details>


---
This comment was created by [Log Detective][log-detective].

Was the provided feedback accurate and helpful? <br>Please vote with :thumbsup:
or :thumbsdown: to help us improve.<br>



[log-detective]: https://log-detective.com/
[contact]: https://github.com/fedora-copr